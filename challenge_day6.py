import os
import requests 
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

def input_code1():
  try:
    code1=input("Where are you from : ")
    print(code1)
    print(f"You live in {infos_filtered[int(code1)][0]}")
    code1 = str(infos_filtered[int(code1)][2])
    
  
  except ValueError:
    print("Input code by number")
    input_code1()
    
  except IndexError:
    print("Input code in range of upper list")
    input_code1()

  return code1

def input_code2():
  try:
    code2=input("What country do you want to exchange : ")
    print(code2)
    print(f"You live in {infos_filtered[int(code2)][0]}")
    code2 = str(infos_filtered[int(code2)][2])
    

  except ValueError:
    print("Input code by number")
    input_code2()
  
  except IndexError:
    print("Input code in range of upper list")
    input_code2()

  return code2


url = "https://www.iban.com/currency-codes"
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
tbody = soup.find("tbody")
tr=tbody.find_all("tr")

infos = []
infos_filtered = []

for i in tr:
  infos.append(i.find_all("td"))


for i in range(len(infos)):
  for j in range(4):
    infos[i][j] = infos[i][j].string

for i in range(len(infos)):
  if 'No universal currency' not in infos[i]:
    infos_filtered.append(infos[i])

print(len(infos_filtered))

for i in range(len(infos_filtered)):
  print(f"#{i}\t{infos_filtered[i][0]}\t{infos_filtered[i][2]}")
''''
try:
  code1=input("Where are you from : ")
  code2=input("What country do you want to exchange : ")
  amount=input("Amount : ")

  print(f"You live in {infos_filtered[int(code1)][0]}")
  print(f"And you wanna exchange your money to {infos_filtered[int(code2)][0]}")

  code1 = str(infos_filtered[int(code1)][2])
  code2 = str(infos_filtered[int(code2)][2])

  url_= f"https://wise.com/gb/currency-converter/{code1}-to-{code2}-rate"
  
  result_=requests.get(url_)
  soup_ = BeautifulSoup(result_.text,'html.parser')

  rate = soup_.find("span", {"class":"text-success"}).string

  print(f'{format_currency(int(amount), code1, locale="ko_KR")} is {format_currency(int(amount)*float(rate), code2, locale="ko_KR")}')

except ValueError:
  print("try number")
'''


code1=input_code1()
code2=input_code2()

print(code1, code2)

amount=input("Amount : ")

url_= f"https://wise.com/gb/currency-converter/{code1}-to-{code2}-rate"

result_=requests.get(url_)
soup_ = BeautifulSoup(result_.text,'html.parser')
rate = soup_.find("span", {"class":"text-success"}).string

print(f'{format_currency(int(amount), code1, locale="ko_KR")} is {format_currency(int(amount)*float(rate), code2, locale="ko_KR")}')