import pymongo
import csv

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["car_sales"]

mycol = mydb["car_name"]
car_name=[]

for x in mycol.find():
  car_name.append([x['ID'],x['car_name'].split('\ufffd')[0],x['min_price'],x['max_price']])

car_name = sorted (car_name, key = lambda x:x[0])
car_name.insert(0,['ID', 'car_name', 'min_price', 'max_price'])

with open('InputProcessing/Output/car_name.csv', 'w', newline="") as csvfile:
  filewriter = csv.writer(csvfile)
  for test in car_name:
    filewriter.writerow(test)
            
print("Car Name Dataset Created as Output\n")

mycol = mydb["sales_list"]
car_sales=[]
car_dup=[]
for x in mycol.find():
  if (x['year']>2013):
    months=12+x['month']
  else:
    months=x['month']
  if (car_dup.count((x['car_id'],months))==0):
    car_sales.append([x['car_id'],months,x['sales']])
    car_dup.append((x['car_id'],months))

car_sales = sorted (car_sales, key = lambda x:(x[0],x[1]))
car_sales.insert(0,['car_id','month','sales'])

with open('InputProcessing/Output/sales_data.csv', 'w', newline="") as csvfile:
      filewriter = csv.writer(csvfile)
      for test in car_sales:
            filewriter.writerow(test)
            
print("Car Sales Dataset Created as Output\n")
