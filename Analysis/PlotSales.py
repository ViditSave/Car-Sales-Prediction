import csv
import matplotlib.pyplot as plt

print("Get Car Sales Data from Dataset")
carList=[['ID','Sales']]
with open('InputProcessing/Output/sales_data.csv','r')as f:
      data = csv.reader(f)
      next(data)
      car_id = 0
      tempSale=0
      for row in data:
            if (car_id == int(row[0])):
                  tempSale+=int(row[2])
            else:
                  newSale=tempSale
                  carList.append([row[0],newSale])
                  car_id+=1
                  tempSale=0
                  tempSale+=int(row[2])
      newSale=tempSale
      carList.append([row[0],newSale])

x=[]
y=[]            
with open('Analysis/Data/salesList.csv', 'w', newline="") as csvfile:
      filewriter = csv.writer(csvfile)
      filewriter.writerow(carList[0])
      for test in carList[1:]:
            if (test[1]!=0):
                  filewriter.writerow(test)
                  x.append(int(test[0]))
                  y.append(int(test[1]))
print("Dataset Processing Completed")

def min_max():
      carName=['ID','Name']
      with open('InputProcessing/Output/car_name.csv','r')as f:
            data = csv.reader(f)
            next(data)
            for row in data:
                  carName.append([int(row[0]),row[1]])
            minName=carName[y.index(min(y))][1]
            maxName=carName[y.index(max(y))][1]
            return "Minimum Sale : "+minName+" -> Sales "+str(min(y))+"\n\nMaximum Sale : "+maxName+" -> Sales "+str(max(y))+"\n"

def scatter():
      plt.plot(x,y,'bo',alpha=0.5)
      plt.title('Scatter Plot of Car Sales')
      plt.xlabel('X-Axis : Car ID'+"\n The Plot represented By Red and Green shows the Minimum and Maximum Sold Cars respectively")
      plt.ylabel('Y-Axis : Total Cars Sold')
      plt.plot(x[y.index(min(y))], min(y), 'ro')
      plt.plot(x[y.index(max(y))], max(y), 'go')
      plt.get_current_fig_manager().window.state('zoomed')
      plt.show()
