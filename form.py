from tkinter import *


root=Tk()
root.resizable(width=False,height=False)
root.geometry("550x500+400+200")
root.iconbitmap(default=r"C:\Users\SANJIB\PycharmProjects\1st\favicon.ico")
name=StringVar()
fname=StringVar()
nation=StringVar()
roll=StringVar()
root.title("student details")
#================def=====================
def addwid(master,text,row,col):
    text = Label(root, text=text, font=("ariel", 12, "bold"), width=15, anchor=E)
    text.grid(row=row, padx=5, pady=5, sticky=E)
    text = Entry(root, background="white", font="bold")

    text.grid(row=row, column=col, padx=10,ipadx=30)









def readfile(name):
    top = Toplevel(root, bg="grey", height=50, width=50)
    top.title("Content")

    okbtn = Button(top, bg="blue", height=2, width=7, text="ok",fg="white",font="bold", command=top.quit)
    okbtn.pack(side=BOTTOM)
    with open(name,"r") as fl:
        f = fl.readline()
        while f!="":
            lab = Label(top, text=f, height=2, width=50, font="bold", bg="grey")
            lab.pack()

            f = fl.readline()

    top.mainloop()




def save():
    try:
        if name.get()=="":
            raise Exception()
        with open(name.get() + '. txt', "w") as fl:
            fl.write("{0:15}\t\t{1:15}\n".format("Name:",name.get()))
            fl.write("{0:15}\t\t{1:15}\n".format("Father's Name:",fname.get()))
            fl.write("{0:15}\t\t{1:15}\n".format("Roll no:",roll.get()))
            fl.write("{0:15}\t\t{1:15}\n".format("Address:",eadd.get("1.0", "end")))
            fl.write("{0:15}\t\t{1:15}\n".format("Nationality:", enation.get()))
    except:
        win2 = Toplevel(root,height=20,width=25)
        win2.title("ERROR")
        label = Label(win2, text="error occur\nfill up the name section", font="bold", bg="red3",height=5,width=25,bd=10)
        label.pack()
        okbttn = Button(win2, height=2,text="ok",bg="orange", width=5, command=win2.quit)
        okbttn.pack(side=BOTTOM)
        okbttn.focus()
        win2.mainloop()
    else:
        readfile(name.get() + '. txt')
    root.quit()


def cancel():
    root.quit()

#===========================wid========================
frame1=Frame(root,height=20,width=50,bg="grey")
frame1.pack(side=TOP)
leb=Label(frame1,text="ANANDA MARG SCHOOL",font=("ariel",25,"bold"),fg="green",padx=5,pady=5).pack()

frame=Frame(root,height=450,width=800,bg="grey")
frame.pack(fill=BOTH,expand=True)
lname=Label(frame,text="Name:",font=("ariel",12,"bold"),width=15,anchor=E,bg="grey")
ename=Entry(frame,background="white",font="bold",textvariable=name,bd=5,takefocus=True)
lname.grid(row=0,padx=5,pady=5,sticky=E)
ename.grid(row=0,column=1,padx=10,pady=5,ipadx=30)
ename.focus()



lfname=Label(frame,text="Father's Name:",font=("ariel",12,"bold"),width=15,anchor=E,bg="grey")
efname=Entry(frame,background="khaki1",font="bold",textvariable=fname,bd=5,takefocus=True)
lfname.grid(row=1,padx=5,pady=5,sticky=E)
efname.grid(row=1,column=1,padx=10,pady=5,ipadx=30)



lroll=Label(frame,text="Roll no:",font=("ariel",12,"bold"),width=15,anchor=E,bg="grey")
eroll=Entry(frame,background="white",font="bold",textvariable=roll,bd=5,takefocus=True)
lroll.grid(row=2,padx=5,pady=5,sticky=E)
eroll.grid(row=2,column=1,padx=10,pady=5,ipadx=30)





ladd=Label(frame,text="Address:",font=("ariel",12,"bold"),width=15,anchor=E,bg="grey")
eadd=Text(frame,background="khaki1",font="bold",height=5,width=20,bd=5,takefocus=True)
ladd.grid(row=3,padx=5,pady=5,sticky=N)
eadd.grid(row=3,column=1,padx=5,pady=7,ipadx=30)



lnation=Label(frame,text="Nationality:",font=("ariel",12,"bold"),width=15,anchor=E,bg="grey")
enation=Entry(frame,background="white",font="bold",textvariable=nation,bd=5,takefocus=True)
lnation.grid(row=4,padx=5,pady=5,sticky=E)
enation.grid(row=4,column=1,padx=10,pady=5,ipadx=30)



#============================btn==================================
svbtn=Button(frame,padx=5,pady=1,text="save",bg="blue",fg="white",font="bold",anchor=E,command=save)
cnbtn=Button(frame,padx=5,pady=1,text="cancel",bg="red3",fg="white",font="bold",anchor=E,command=cancel)
svbtn.grid(row=5,column=1,padx=5,pady=30,sticky=E)
cnbtn.grid(row=5,padx=5,column=1,pady=30,sticky=W)



#addwid()
root.mainloop()