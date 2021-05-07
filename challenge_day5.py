import os
import requests as rq
from bs4 import BeautifulSoup as soup


def output_code():
  try:
    num = int(input('Select number right here: '))
    print('You choose ', info_list_2[num][0],'\nThe currency code is ',info_list_2[num][2])
    output_code()
    
  except IndexError:
    print("The number is out of range. Try a number in range")
    output_code()

  except ValueError:
    print('That is not a number. Try input by number')
    output_code()



os.system("clear")
url = "https://www.iban.com/currency-codes"

result = rq.get(url)
soup = soup(result.text, 'html.parser')

tbody = soup.find("tbody")

tr = tbody.find_all('tr')

info_list = []
info_list_2 = []

for td in tr:
  info_list.append(td.find_all('td'))

for i in range(len(info_list)):
  for j in range(4):
    info_list[i][j] = info_list[i][j].string

for i in range(len(info_list)):
  if 'No universal currency' not in info_list[i]:
    info_list_2.append(info_list[i])


print('HELLO! Please choose a country by selecting number\n')

for i in range(len(info_list_2)):
  print('#',i,' ',info_list[i][0],'\n')

output_code()