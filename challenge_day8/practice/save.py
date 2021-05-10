import csv

def save_as_csv(brand_name, contents):
  if '/' in str(brand_name):
    brand_name= brand_name.replace("/",'_')  
  file = open(f"{brand_name}.csv", mode='w')
  writer = csv.writer(file)
  writer.writerow(['place','title', 'worktime', 'pay', 'reg time'])

  for i in range(len(contents)):
    writer.writerow(contents[i])
  