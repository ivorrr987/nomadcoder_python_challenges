import os
import csv
import requests
from bs4 import BeautifulSoup

def get_max_page(url):
  url = requests.get(url)
  soup = BeautifulSoup(url.text, 'html.parser')

  how_many_info = soup.select_one('#NormalInfo > p.jobCount > strong')
  try:
    how_many_info = str(how_many_info.string)
    how_many_info = how_many_info.replace(',','')
    how_many_info = float(how_many_info)
    how_many_info = int(how_many_info)
    max_page = (how_many_info//50)+1
  except AttributeError:
    max_page = 1

  return max_page