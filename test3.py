from tkinter import *
from tkinter.ttk import *

def convert(uin, CurrencyRates=None):
    from forex_python.converter import CurrencyRates
    c1=CurrencyRates()
    sum=c1.convert(uin)
    return sum

window=Tk()
window.configure(background="lightblue")
window.title("Currency Converter by :Omkar,Mahesh and Antariks")
l0=Label(window,text="WELCOME TO CURRENCY CONVERTER",font=("Arial Bold",16),background="lightgreen")
l0.grid(column=1,row=0)
l1=Label(window,text="Enter amount to be converted in Dollars($) or Rupees(₹)",font=("Calibri",16),background="pink")
l1.grid(column=1,row=1)

def clicked():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()  # force_decimal=True
    uin = int(txt.get())
    sum = c.convert('USD', 'INR', uin)

    l2.configure(text="The Amount in INR(₹):"+str(sum))
def clicked2():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()  # force_decimal=True
    uin = int(txt.get())
    sum = c.convert('INR', 'USD', uin)

    l3.configure(text="The Amount in USD($):"+str(sum))


ra=Radiobutton(window,text="Dollars($)",value=1,command=clicked)
ra.grid(column=1,row=3)

ra1=Radiobutton(window,text="Rupees(₹)",value=2,command=clicked2)
ra1.grid(column=1,row=4)


txt=Entry(window,width=16)
txt.grid(column=1,row=2)



l2=Label(window,text="",background="light blue")
l2.grid(column=1,row=6)

l3=Label(window,text="",background="light blue")
l3.grid(column=1,row=10)

window.geometry("500x400")
window.mainloop()
