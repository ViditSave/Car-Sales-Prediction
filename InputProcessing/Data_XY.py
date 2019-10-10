import csv

print("Data Processing for Prediction month to sales\n")
carList=[]
with open('InputProcessing/Output/sales_data.csv','r')as f:
      data = csv.reader(f)
      next(data)
      car_id = 0
      tempx=[]
      tempy=[]
      for row in data:
            if (car_id == int(row[0])):
                  tempx.append(int(row[1]))
                  tempy.append(int(row[2]))
            else:
                  newx = tempx[:]
                  newy = tempy[:]
                  carList.append([car_id,newx,newy])
                  car_id+=1
                  tempx.clear()
                  tempy.clear()
                  tempx.append(int(row[1]))
                  tempy.append(int(row[2]))
      
      newx = tempx[:]
      newy = tempy[:]
      carList.append([car_id,newx,newy])

carList = sorted (carList, key = lambda x:(len(x[1])), reverse=True)
carList=carList[:5]
for i in carList:
      print(i)

carName=[]
with open('InputProcessing/Output/car_name.csv','r')as f:
      data = csv.reader(f)
      next(data)
      for row in data:
            carName.append(row[1])
            
with open('Analysis/Data/month_sales_xy.csv', 'w', newline="") as csvfile:
      filewriter = csv.writer(csvfile)
      for test in carList:
            filewriter.writerow([test[0],carName[test[0]],test[1],test[2]     ])
print("Processed Data in X-Y for Month-Sales")
