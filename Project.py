import sys
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

sys.path.append('InputProcessing/')
import mongodb
import Data_XY        

def Price_Graph():
    sys.path.append('Analysis/')
    import PlotPrice
    
    priceWin = Toplevel(window)
    priceWin.state('zoomed')
    priceWin.configure(background='white')

    la0 = Label(priceWin, text="Car Price Graphs", font=("Arial Bold", 50), bg="white", fg="midnight blue")
    la1 = Label(priceWin, text=PlotPrice.min_max(), font=("Arial Bold", 30), bg="white", fg="midnight blue")
    bt0 = Button(priceWin, text="Show Scatter Graph", command=PlotPrice.scatter, font=("Arial Bold", 30), bg="LightSkyBlue1", fg="midnight blue", height=1, width=21)
    bt1 = Button(priceWin, text="Show Histogram", command=PlotPrice.histogram, font=("Arial Bold", 30), bg="LightSkyBlue1", fg="midnight blue", height=1, width=21)

    la0.grid(columnspan=2, row=0, pady=100)
    la1.grid(columnspan=2, row=1, pady=15)
    bt0.grid(column=0, row=3, pady=15, padx=80)
    bt1.grid(column=1, row=3, pady=15, padx=80)
      
def Sales_Graph():
    sys.path.append('Analysis/')
    import PlotSales
    
    salesWin = Toplevel(window)
    salesWin.state('zoomed')
    salesWin.configure(background='white')

    la0 = Label(salesWin, text="Car Sales Graphs", font=("Arial Bold", 50), bg="white", fg="midnight blue", width=33)
    la1 = Label(salesWin, text=PlotSales.min_max(), font=("Arial Bold", 30), bg="white", fg="midnight blue")
    bt0 = Button(salesWin, text="Show Scatter Graph", command=PlotSales.scatter, font=("Arial Bold", 30), bg="LightSkyBlue1", fg="midnight blue", height=1, width=21)
    
    la0.grid(row=0, pady=100)
    la1.grid(row=1, pady=15)
    bt0.grid(row=3, pady=15, padx=80)
    
def Month_Graph():

    sys.path.append('Analysis/')
    import PlotMonthSale
    
    monthWin = Toplevel(window)
    monthWin.state('zoomed')
    monthWin.configure(background='white')

    la0 = Label(monthWin, text="Car Yearly Sales Graphs", font=("Arial Bold", 50), bg="white", fg="midnight blue", width=33)
    bt0 = Button(monthWin, text="2015 Sales Linear Regression", command=PlotMonthSale.sales2015l, font=("Arial Bold", 25), bg="LightSkyBlue1", fg="midnight blue", height=1, width=30)
    bt1 = Button(monthWin, text="2015 Sales Polynomial Regression", command=PlotMonthSale.sales2015p, font=("Arial Bold", 25), bg="LightSkyBlue1", fg="midnight blue", height=1, width=30)
    bt2 = Button(monthWin, text="2016 Sales Linear Regression", command=PlotMonthSale.sales2016l, font=("Arial Bold", 25), bg="LightSkyBlue1", fg="midnight blue", height=1, width=30)
    bt3 = Button(monthWin, text="2016 Sales Polynomial Regression", command=PlotMonthSale.sales2016p, font=("Arial Bold", 25), bg="LightSkyBlue1", fg="midnight blue", height=1, width=30)
    
    la0.grid(row=0, pady=110, columnspan=2)
    bt0.grid(row=1, column=0, pady=25)
    bt1.grid(row=1, column=1, pady=25)
    bt2.grid(row=2, column=0, pady=25)
    bt3.grid(row=2, column=1, pady=25)
    
def Sales_Prediction():

    sys.path.append('Analysis/')
    import PredictSales

    predWin = Toplevel(window)
    predWin.state('zoomed')
    predWin.configure(background='white')

    la0 = Label(predWin, text="Car Sales Prediction", font=("Arial Bold", 50), bg="white", fg="midnight blue", width=33)
    values=PredictSales.sendCarList()
    for i in range (len(values)):
        tname="button"+str(i)
        tname=Button(predWin, text=values[i], command=lambda i=i: PredictSales.sendXY(i), font=("Arial Bold", 30), bg="LightSkyBlue1", fg="midnight blue", width=20)
        tname.grid(row=int(i+1), pady=5)
    la0.grid(row=0, pady=60)
    

    
window = Tk()
window.title("Car Dealership")
window.state('zoomed')
window.configure(background='white')

lab1 = Label(window, text="Car Sales Analysis", font=("Arial Bold", 50),anchor="center", bg="white", fg="midnight blue")
btn1 = Button(window, text="Car Price Graphs", command=Price_Graph, font=("Arial Bold", 30), bg="LightSkyBlue1", fg="midnight blue", height=1, width=21)
btn2 = Button(window, text="Car Sales Graph", command=Sales_Graph, font=("Arial Bold", 30), bg="LightSkyBlue1", fg="midnight blue", height=1, width=21)
btn3 = Button(window, text="Yearly Sales Prediction", command=Month_Graph, font=("Arial Bold", 30), bg="LightSkyBlue1", fg="midnight blue", height=1, width=21)
btn4 = Button(window, text="Car Sales Prediction", command=Sales_Prediction, font=("Arial Bold", 30), bg="LightSkyBlue1", fg="midnight blue", height=1, width=21)
img = ImageTk.PhotoImage(Image.open("background.jpg"))
img1 = Label(window, image = img)

lab1.grid(row=0, columnspan=2, pady=40)
btn1.grid(column=0, row=1, pady=15)
btn2.grid(column=1, row=1, pady=15)
btn3.grid(column=0, row=2, pady=15)
btn4.grid(column=1, row=2, pady=15)
img1.grid(row=4, columnspan=2, pady=15)
window.mainloop()
