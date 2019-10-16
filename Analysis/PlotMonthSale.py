import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

print("Get Car Sales Data from Dataset")
carList=[]
with open('InputProcessing/Output/sales_data.csv','r')as f:
      data = csv.reader(f)
      next(data)
      for row in data:
            carList.append([int(row[1]),int(row[2])])
            
      carList=sorted(carList, key=lambda x: int(x[0]))
      carList.insert(0,['Month', 'Sales'])

with open('Analysis/Data/yearlysalesList.csv', 'w', newline="") as csvfile:
      filewriter = csv.writer(csvfile)
      for test in carList:
            filewriter.writerow(test)
print("Dataset Processing Completed")

monthList=carList[1:]
month=1
totalSale=0
finalSaleX=[]
finalSaleY=[]
for row in monthList:
      if (row[0]==month):
            totalSale+=row[1]
      else:
            finalSaleX.append(month)
            finalSaleY.append(totalSale)
            totalSale=row[0]
            month+=1

finalSaleX.append(month)
finalSaleY.append(totalSale)

def sales2015l():
      Y=np.array(finalSaleY[:13])
      X=np.array([i for i in range(1,len(Y)+1)]).reshape((-1,1))
      plot_salesl(X,Y,'2015')
      
def sales2016l():
      Y=np.array(finalSaleY[12:])
      X=np.array([i for i in range(1,len(Y)+1)]).reshape((-1,1))
      plot_salesl(X,Y,'2016')
      
def plot_salesl(X,Y,year):
      regression_model = LinearRegression()
      regression_model.fit(X, Y)
      y_predicted = regression_model.predict(X)

      slope=float(str(regression_model.coef_)[1:-1])
      inter=regression_model.intercept_
      
      text="\n( Slope : "+str(round(slope, 2))+", Intercept : "+str(round(inter, 2))+" )\n"
      if (slope<0):
            text+="Decreasing Graph means the Monthly Sales reduces in the following Months"
      else:
            text+="Increasing Graph means the Monthly Sales increases in the following Months"

      nextMonth=12

      newVal1= round(slope*(nextMonth+1)+inter, 2)
      newVal2= round(slope*(nextMonth+2)+inter, 2)
      newVal3= round(slope*(nextMonth+3)+inter, 2)

      newVal1= newVal1 if newVal1>0 else 0
      newVal2= newVal2 if newVal2>0 else 0
      newVal3= newVal3 if newVal3>0 else 0

      plt.title('Car Sales Prediction for the Year '+year+text)
      plt.xlabel('X-Axis : Months'+"\nPredicted Value of Sales for Month "+str(nextMonth+1)+" is "+str(newVal1)+", Month "+str(nextMonth+2)+" is "+str(newVal2)+", Month "+str(nextMonth+3)+" is "+str(newVal3))
      plt.ylabel('Y-Axis :  Sales')
      plt.plot(X,y_predicted, color='r')
      plt.plot(X,Y,'bo',alpha=0.5)
      plt.plot(nextMonth+1,newVal1,'go')
      plt.plot(nextMonth+2,newVal2,'go')
      plt.plot(nextMonth+3,newVal3,'go')
      plt.get_current_fig_manager().window.state('zoomed')
      plt.show()

def sales2015p():
      Y=np.array(finalSaleY[:12])
      X=np.array([i for i in range(1,len(Y)+1)]).reshape((-1,1))
      plot_salesp(X,Y,'2015')
      
def sales2016p():
      Y=np.array(finalSaleY[12:])
      X=np.array([i for i in range(1,len(Y)+1)]).reshape((-1,1))
      plot_salesp(X,Y,'2016')

def plot_salesp(X,y,year):
      from sklearn.preprocessing import PolynomialFeatures 

      lin = LinearRegression() 
      lin.fit(X, y) 
      poly = PolynomialFeatures(degree = 3) 
      X_poly = poly.fit_transform(X) 
      poly.fit(X_poly, y) 
      lin2 = LinearRegression() 
      lin2.fit(X_poly, y)

      nextMonth=12

      newVal1= lin2.predict(poly.fit_transform(np.array(nextMonth+1).reshape((-1,1))))[0]
      newVal2= lin2.predict(poly.fit_transform(np.array(nextMonth+2).reshape((-1,1))))[0]
      newVal3= lin2.predict(poly.fit_transform(np.array(nextMonth+3).reshape((-1,1))))[0]
      
      #plt.scatter(X, y, color = 'blue') 
      plt.plot(X, lin2.predict(poly.fit_transform(X)), color = 'red') 
      plt.title('Car Sales Prediction for the Year '+year)
      plt.xlabel('X-Axis : Months'+"\nPredicted Value of Sales for Month "+str(nextMonth+1)+" is "+str(round(newVal1,2))+", Month "+str(nextMonth+2)+" is "+str(round(newVal2,2))+", Month "+str(nextMonth+3)+" is "+str(round(newVal3,2)))
      plt.ylabel('Y-Axis :  Sales')
      plt.plot(X,y,'bo',alpha=0.5)
      plt.plot(nextMonth+1,newVal1,'go')
      plt.plot(nextMonth+2,newVal2,'go')
      plt.plot(nextMonth+3,newVal3,'go')
      plt.get_current_fig_manager().window.state('zoomed')
      plt.show()
