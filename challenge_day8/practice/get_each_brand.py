import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")

def get_each_brand(each_brand_url, max_page):
  alba_list = []
  for page in range(max_page):
    brand_url = requests.get(f"{each_brand_url}?page={page+1}")
    brand_soup = BeautifulSoup(brand_url.text, 'html.parser')

    
    table = brand_soup.select_one('#NormalInfo > table')
    tbody = table.find("tbody")

    tr=tbody.find_all("tr", {"class":""})

    for i in range(len(tr)):
      each_info = []

      try:
        loc = tr[i].find("td", {"class":"local first"})
        loc = loc.get_text()
        loc = loc.replace("\xa0","")
      except AttributeError:
        loc = 'Empty'
      each_info.append(loc)
    
      try:
        alba_title_td = tr[i].find("td", {"class":"title"})
        alba_title_a = alba_title_td.find("a")
        alba_title = alba_title_a.find("span", {"class":"company"}) 
        alba_title = str(alba_title.string)
      except AttributeError:
        alba_title = 'Empty'
      

      try:
        worktime_td = tr[i].find("td", {"class":"data"})
        worktime = worktime_td.find("span")
        worktime = str(worktime.string)
      
      except AttributeError:
        worktime = 'Empty'
      

      try:
        pay_td = tr[i].find("td", {"class":"pay"})
        pay_period = pay_td.find("span", {"class":"payIcon"})
        pay = pay_td.find("span", {"class":"number"})
        pay_period = str(pay_period.string)
        pay = str(pay.string)
        pay = pay_period + ' ' + pay
      except AttributeError:
        pay = 'Empty'

      try:
        reg_time = tr[i].find("td", {"class":"regDate"})
        reg_time = reg_time.get_text()
      
      except AttributeError:
        reg_time = 'Empty'

      each_info=[loc, alba_title, worktime, pay, reg_time]
      alba_list.append(each_info)

  return alba_list

