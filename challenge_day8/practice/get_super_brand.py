import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")

def get_super_brand(alba_url):
  alba_url = "http://www.alba.co.kr"
  alba_html = requests.get(alba_url)
  alba_soup = BeautifulSoup(alba_html.text, 'html.parser')

  super_brand = alba_soup.find("div", {"id":"MainSuperBrand"})
  logo = super_brand.find_all("span",{"class":"logo"})
  li_impact= super_brand.find_all("li", {"class":"impact"})

  company_and_url = {}

  for i in range(len(li_impact)):
    company_and_url[str(li_impact[i].find("span",{"class":"company"}).string)]=li_impact[i].find("a")["href"]

  return company_and_url