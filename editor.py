from tkinter import *


class edit:

    cntn=""

    def save(self):
        global cntn
        cntn = self.text.get("1.0", "end")
        self.namef()
        nm=self.name.get()
        try:
            with open('C:\\Users\\SANJIB\\Documents\\' + nm + ".txt", "a") as fl:
                fl.write(cntn)
        except:
            win2 = Toplevel(root)
            win2.title("ERROR")
            label=Label(win2,text="error occur",font="bold",bg="red")
            label.pack()
            okbttn=Button(win2,height=1,width=2)
            okbttn.pack(side=BOTTOM,command=win2.quit())
            win2.mainloop()

        root.quit()


    def namef(self):
        win1=Toplevel(root)
        win1.title("FILE NAME")

        def ok():
            win1.quit()
            return
        label=Label(win1,text="Name:",font="bold")
        label.grid(row=0,sticky=E)
        namen = Entry(win1,font="bold",textvariable=self.name)
        namen.grid(row=0, column=1)
        okbtn=Button(win1,text="ok",font="bold",fg="white",bg="blue",command=lambda:ok())
        okbtn.grid(row=1,sticky=E)
        win1.mainloop()

    def __init__(self,root,name):
        root.iconbitmap(default=r'C:\Users\SANJIB\PycharmProjects\1st\notepad.ico')
        #global cntn
        root.title("MY NOTEPAD")
        self.name=name
        save=Button(root,text="save",height=1,width=5,command=self.save,font="bold",bg="green")
        save.grid(row=0,sticky=W)
        #frame=Frame(root,height=25,width=100)
        #frame.grid(row=0,padx=100,pady=50)
        self.text=Text(root,height=25,width=100,font=("bold"))
        self.text.grid()






root=Tk()
name=StringVar()
editor=edit(root,name)

root.mainloop()