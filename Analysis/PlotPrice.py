import csv
import matplotlib.pyplot as plt

print("Get Average Car Price from Dataset\n")
carList=[['ID','Name','Price']]
with open('InputProcessing/Output/car_name.csv','r')as f:
      data = csv.reader(f)
      next(data)
      for row in data:
            t=(int(row[2])+int(row[3]))//2
            carList.append([row[0],row[1],t])
name=[]
x=[]
y=[]
with open('Analysis/Data/priceList.csv', 'w', newline="") as csvfile:
      filewriter = csv.writer(csvfile)
      filewriter.writerow(carList[0])
      for test in carList[1:]:
            filewriter.writerow(test)
            x.append(int(test[0]))
            name.append(test[1])
            y.append(int(test[2]))
print("Dataset Processing Completed.\n")

def min_max():
      minName=name[y.index(min(y))]
      maxName=name[y.index(max(y))]
      return "Minimum Price : "+minName+" -> Rs "+str(min(y))+"\n\nMaximum Price : "+maxName+" -> Rs "+str(max(y))+"\n"

def scatter():
      plt.plot(x,y,'bo',alpha=0.5)
      plt.title('Scatter Plot of Car Price')
      plt.xlabel('X-Axis : Car ID'+"\n The Plot represented By Red and Green shows the Minimum and Maximum Priced Cars respectively")
      plt.ylabel('Y-Axis : Price of Car')
      plt.plot(x[y.index(min(y))], min(y), 'ro')
      plt.plot(x[y.index(max(y))], max(y), 'go')
      plt.get_current_fig_manager().window.state('zoomed')
      plt.show()

def histogram():
      axs = plt.hist(y, bins=25, facecolor='blue', alpha=0.7)
      plt.title('Histogram of Car Price')
      plt.xlabel('X-Axis : Price of Car')
      plt.ylabel('Y-Axis : Number of Cars')
      plt.get_current_fig_manager().window.state('zoomed')
      plt.show()
