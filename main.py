from tkinter import *
import os

root=Tk()
root.title('Temprature Converter')
root.resizable(False,False)

def celsiusToFahrenheit():
    celsius=float(txtfld1.get())
    fahrenheit=(celsius*9/5)+32
    txtfld2.delete(0,END)
    txtfld2.insert(0,str(fahrenheit))

def FahrenheitToCelsius():
    fahrenheit=float(txtfld1.get())
    celsius=(fahrenheit-32)*5/9
    txtfld2.delete(0,END)
    txtfld2.insert(0,str(celsius))

playground=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),width=55)
playground.grid(columnspan=6)
playground.insert(END,"Temprature Converter")

lb1=Label(root,text="Enter Temprature",font=('arial',13),bg="black",fg="white",padx=10,pady=10,border=1)
lb1.place(x=80, y=70)

txtfld1=Entry(root, text="This is Entry Widget", bd=5,border=5,bg="black",fg="white")
txtfld1.place(x=80, y=90)
txtfld1.grid(row=0,column=0)

lb2=Label(root,text="Converted Temprature",font=('arial',13),bg="black",fg="white",padx=10,pady=10,border=1)
lb2.place(x=250, y=70)


txtfld2=Entry(root, text="This is Entry Widget 1", bd=5,border=5,bg="black",fg="white")
txtfld2.place(x=270, y=109)

celsiusbtn=Button(root,text="Celsius To Fahrenheit",command=celsiusToFahrenheit)
celsiusbtn.config(font=('arial',20),bg="black",fg="white",padx=10,pady=10,border=1)
celsiusbtn.grid(row=1,column=0)

Fahrenheitbtn=Button(root,text="Fahrenheit To Celsius")
Fahrenheitbtn.config(font=('arial',20),bg="black",fg="white",padx=10,pady=10,border=1)
Fahrenheitbtn.grid(row=1,column=1)

root.mainloop()