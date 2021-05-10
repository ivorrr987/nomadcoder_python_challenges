import os
import csv
import requests
from bs4 import BeautifulSoup


def get_each_brand(brand_url):
  brand_url = requests.get(brand_url)
  brand_soup = BeautifulSoup(brand_url.text, 'html.parser')

  infos = brand_soup.find_all("tr")
  lists=[]

  

  return infos

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


os.system("clear")

alba_url = "http://www.alba.co.kr"

brand_list = get_super_brand(alba_url)

brand_url = requests.get(get_each_brand(brand_list['세븐일레븐']))
brand_soup = BeautifulSoup(brand_url.text, 'html.parser')

infos = brand_soup.find_all("tr")

local= infos.find_all("td", {"class":"local"})
print(local)

lists=[]
a_list=[]
''''
places=infos.find("td",{"class":"local first"})
print(places)
'''
