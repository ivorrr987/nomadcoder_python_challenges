import os
import csv
import requests
from bs4 import BeautifulSoup
from get_super_brand import get_super_brand
from get_each_brand import get_each_brand
from save import save_as_csv
from get_max_page import get_max_page

os.system("clear")

alba_url = "http://www.alba.co.kr"

print("Alba info scrapping... ")

brand_list = get_super_brand(alba_url)

list_max_length = len(brand_list)
nth_of_list = 1

for brand in brand_list.keys():
  print(f"{brand} is being stored. If it's done, You can see the URL. [{nth_of_list}/{list_max_length}]")

  max_page=get_max_page(brand_list[brand])
  save_as_csv(brand, get_each_brand(brand_list[brand],max_page))

  print(brand_list[brand])
  print()
  
  nth_of_list += 1  

print("Done!")
