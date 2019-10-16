import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

print("Predict Car Sales from Dataset\n")
#['ID','Name','Month','Sales']
carList=[]

with open('Analysis/Data/month_sales_xy.csv','r')as f:
      data = csv.reader(f)
      for row in data:
            carList.append(row)

def sendCarList():
      return [i[1] for i in carList]

def sendXY(carNum):
      selCar=carList[carNum]
      carx=[]
      cary=[]
      for i in (selCar[2][1:-1]).split(","):
            carx.append(int(i))
      for i in (selCar[3][1:-1]).split(","):
            cary.append(int(i))
      carx=np.array(carx).reshape((-1,1))
      cary=np.array(cary)

      regression_model = LinearRegression()
      regression_model.fit(carx, cary)
      y_predicted = regression_model.predict(carx)

      slope=float(str(regression_model.coef_)[1:-1])
      inter=regression_model.intercept_
      
      text="\n( Slope : "+str(slope)+", Intercept : "+str(inter)+" )\n"
      if (slope<0):
            text+="Decreasing Graph means Sales of the car reduces in the next Months"
      else:
            text+="Increasing Graph means Sales of the car increases in the next Months"

      newVal25= round(slope*25+inter, 2)
      newVal26= round(slope*26+inter, 2)
      newVal27= round(slope*27+inter, 2)

      newVal25= newVal25 if newVal25>0 else 0
      newVal26= newVal26 if newVal26>0 else 0
      newVal27= newVal27 if newVal27>0 else 0
      
      plt.scatter(carx, cary, s=10)
      plt.plot(carx, y_predicted, color='r')
      plt.title('Car Sales Prediction for '+selCar[1]+text)
      plt.xlabel('X-Axis : Months'+"\nPredicted Value of Sales for Month 25 is "+str(newVal25)+", Month 26 is "+str(newVal26)+", Month 27 is "+str(newVal27))
      plt.ylabel('Y-Axis : Monthly Sales')
      plt.plot(25,newVal25,'go')
      plt.plot(26,newVal26,'go')
      plt.plot(27,newVal27,'go')
      plt.get_current_fig_manager().window.state('zoomed')
      plt.show()
