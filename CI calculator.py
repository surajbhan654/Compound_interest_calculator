
from tkinter import *
from turtle import end_fill

win = Tk()
win.title("Compound Interest Calculator")

win.maxsize(400,300)
win.minsize(400,300)
#win.geometry("400x400")


def calculate():
    principle= int(Principle.get())
    rate=int(Rate.get())
    time=int(Time.get())
    CI = principle * (pow((1 + rate / 100), time))
    Compound_interest.insert(INSERT,CI)

def delete_text():
    Principle.delete(0,END)
    Rate.delete(0,END)
    Time.delete(0,END)
    Compound_interest.delete(0,END)
    

label1 = Label(win,text="Principle Ammount  : ")
label2 = Label(win,text="Rate(%)   : ")
label3 = Label(win,text="Time(year)  : ")

label4 = Label(win,text="Compount Interest  :")

label1.grid(row=0,column=0,padx=15,pady=15)
label2.grid(row=1,column=0,padx=15,pady=15)
label3.grid(row=2,column=0,padx=15,pady=15)
label4.grid(row=3,column=0,padx=15,pady=15)



Principle=Entry(win)
Rate=Entry(win)
Time=Entry(win)
Compound_interest=Entry(win)

Principle.grid(row=0,column=1,padx=15,pady=15)
Rate.grid(row=1,column=1,padx=15,pady=15)
Time.grid(row=2,column=1,padx=15,pady=15)
Compound_interest.grid(row=3,column=1,padx=15,pady=15)


button1=Button(text="Submit",command=calculate,width=10)
button2=Button(text="Clear", command=delete_text,width=10)
button3 = Button(win, text = "Exit",  fg = "black", command = lambda:exit(), width=10)

button1.grid(row=4,column=0,padx=10,pady=15)
button2.grid(row=4,column=1,padx=10,pady=15)
button3.grid(row=4,column=2,padx=10,pady=15)

win.mainloop()
