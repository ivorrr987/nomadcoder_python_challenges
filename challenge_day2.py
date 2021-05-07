"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""

def is_on_list(days, day_name):
  is_on_value = False
  for i in range(len(days)):
    if days[i] == day_name:
      is_on_value = True

  return is_on_value

def get_x(days, num):

  return days[num]

def add_x(days, day_name):
  days.append(day_name)

def remove_x(days, day_name):
  days.remove(day_name)
  
# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #





