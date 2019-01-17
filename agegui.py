from tkinter import *

import age


root=Tk()
root.title("age counter")
root.geometry("500x250+400+300")
date=StringVar()
month=StringVar()
year=StringVar()
text=StringVar()

def calculate():
    d=int(date.get())
    m=int(month.get())
    y=int(year.get())
    lst=[d,m,y]
    days,months,years=age.age(lst)
    text.set(str(years)+" years "+str(months)+" months "+str(days)+" days ")
    rslt1 = Label(frame, textvariable=text, font="bold", fg="gold", bg="green", height=3,width=30)
    rslt1.grid(row=1, column=1,columnspan=5)

def reset():
    edate.delete(0)
    emon.delete(0)
    eyar.delete(0)
    date.set("")
    month.set("")
    year.set("")
    text.set("")



frame=Frame(root,height=500,width=300,bg="green")
frame.pack(fill=BOTH,expand=True)
dat=Label(frame,text="day",font="bold",fg="gold",bg="green",padx=5,pady=3)
dat.grid(row=0,column=0,padx=5,pady=5,ipadx=5,ipady=5)
edate=Entry(frame,textvariable=date,width=4,font="bold")
edate.grid(row=0,column=1,padx=5,pady=5,ipadx=3,ipady=5)
edate.focus()


mon=Label(frame,text="month",font="bold",fg="gold",bg="green",padx=5,pady=3)
mon.grid(row=0,column=2,padx=5,pady=5,ipadx=5,ipady=5)
emon=Entry(frame,textvariable=month,width=4,font="bold")
emon.grid(row=0,column=3,padx=5,pady=5,ipadx=3,ipady=5)


yar=Label(frame,text="year",font="bold",fg="gold",bg="green",padx=5,pady=3)
yar.grid(row=0,column=4,padx=5,pady=5,ipadx=5,ipady=5)
eyar=Entry(frame,textvariable=year,width=5,font="bold")
eyar.grid(row=0,column=5,padx=5,pady=5,ipadx=5,ipady=5)

rslt=Label(frame,text="result",font="bold",fg="gold",bg="green",height=3,width=5)
rslt.grid(row=1,column=0,padx=6)




cal=Button(frame,text="calculate",bg="blue",fg="white",height=2,width=7,command=calculate)
cal.grid(row=2,column=3,padx=5,pady=5)
rst=Button(frame,text="reset",bg="red",fg="white",height=2,width=7,command=reset)
rst.grid(row=3,column=3,padx=5,pady=5)

root.mainloop()