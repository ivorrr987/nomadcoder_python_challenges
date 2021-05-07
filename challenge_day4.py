import requests as rq

def check_http(input_array):
  for i in range(len(input_array)):
    input_array[i]=input_array[i].strip(' ')
    if "http" not in input_array[i]:
      input_array[i] = "http://"+input_array[i]

def check_online(input_array):
  for i in range(len(input_array)):

    try:
      result=rq.get(input_array[i])
      result_code = result.status_code
    except rq.exceptions.ConnectionError:
      result_code = '404'
    

    if result_code == 200:
      print(input_array[i]," is up!")
    else:
      print(input_array[i]," is down!")

def check_restart(): 

  print("Do you want to start over? [y/n]")
  start = input()

  if start == 'y':
    init()
  elif start =='n':
    print("bye")
  else:
    print("That's not a valid answer")
    check_restart()




def init():
  print("Welcome to isItDown.py!")
  print("please write down a URL or URLs you want to check (seperated by comma) :")
  URLs = input().split(',')
  
  check_http(URLs)
  check_online(URLs)
  check_restart()


init()

  

