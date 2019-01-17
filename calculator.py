from tkinter import*
import math


op = ""
val="0+"
class calc:



    def __init__(self,root,inp):
        root.iconbitmap(r'C:\Users\SANJIB\PycharmProjects\1st\calc.ico')




        # ========entry=====
        ent = Entry(root,justify=RIGHT,textvariable=inp,font=("bold"),bd=8,bg="powder blue")
        ent.pack(side=TOP, padx=20, pady=15, expand=False, ipadx=10, ipady=5)

        mframe = Frame(root, height=550, width=250,bd=8,relief=SUNKEN,bg="powder blue")
        mframe.pack()

        # =======button========

        def press(num):
            global op,val
            oprt=["1","2","3","4","5","6","7","8","9"]

#============display==========
            if num=="s":
                num="^2"
            elif num=="c":
                num="^3"
            op = op + (num)
            inp.set(op)



#===========value==========
            if num=="π":
                val=val+str(math.pi)
            else:
                val = val + (num)

            if num==")":
                for i in range(len(val),0,-1):
                    p=val[i]+p
                    if val[i]=="(":
                        p=p[1:-1]


            if val[-2]=="^":
                p=val[-1]
                b=val[-3]
                t=str(pow(int(b),int(p)))
                val=val[:-3]+t



            if val[-2]=="√":
                p=int(val[-1])
                t=str(math.sqrt(p))
                val=val[:-2]+t

            if val[-2]=="r":
                p=int(val[-1])
                v=val[-3]
                t=str(int(p)**(1/(int(v))))
                val=val[:-3]+t


        def presse():
            global val
            try:
                result = str(eval(val))
                inp.set(result)
                val = result
            except:
                result="math error"
                pressac()
                inp.set(result)


        def pressac():
            global op,val
            op=""
            val="0+"
            inp.set(op)
        def clear():
            global op,val
            val = val[0:-1]
            op = op[0:-1]
            inp.set(op)




        button1 = Button(mframe, text="1", height=1, width=5, command=lambda:press("1"),borderwidth=5,font="bold")
        button2 = Button(mframe, text="2", height=1, width=5, command=lambda:press("2"),borderwidth=5,font="bold")
        button3 = Button(mframe, text="3", height=1, width=5, command=lambda:press("3"),borderwidth=5,font="bold")
        button4 = Button(mframe, text="4", height=1, width=5, command=lambda:press("4"),borderwidth=5,font="bold")
        button5 = Button(mframe, text="5", height=1, width=5, command=lambda:press("5"),borderwidth=5,font="bold")
        button6 = Button(mframe, text="6", height=1, width=5, command=lambda:press("6"),borderwidth=5,font="bold")
        button7 = Button(mframe, text="7", height=1, width=5, command=lambda:press("7"),borderwidth=5,font="bold")
        button8 = Button(mframe, text="8", height=1, width=5, command=lambda:press("8"),borderwidth=5,font="bold")
        button9 = Button(mframe, text="9", height=1, width=5, command=lambda:press("9"),borderwidth=5,font="bold")
        button0 = Button(mframe, text="0", height=1, width=5, command=lambda:press("0"),borderwidth=5,font="bold")
        buttonp = Button(mframe, text="+", height=5, width=5, command=lambda:press("+"),borderwidth=5,font="bold")
        buttons = Button(mframe, text="-", height=1, width=5, command=lambda:press("-"),borderwidth=5,font="bold")
        buttonm = Button(mframe, text="x", height=1, width=5, command=lambda:press("*"),borderwidth=5,font="bold")
        buttond = Button(mframe, text="/", height=1, width=5, command=lambda:press("/"),borderwidth=5,font="bold")
        buttone = Button(mframe, text="=", height=1, width=5, command=lambda:presse(),borderwidth=5,font="bold")
        buttonac = Button(mframe, text="AC", height=1, width=5, command=lambda:pressac(),borderwidth=5,font="bold",bg="red")
        buttonc = Button(mframe, text="C", height=1, width=5, command=lambda: clear(),borderwidth=5,font="bold",bg="blue")


        buttonpnt = Button(mframe, text=".", height=1, width=5, command=lambda: press("."),borderwidth=5,font="bold")
        buttonb1 = Button(mframe, text="(", height=1, width=5, command=lambda: press("("),borderwidth=5,font="bold")
        buttonb2 = Button(mframe, text=")", height=1, width=5, command=lambda: press(")"), borderwidth=5, font="bold")
        buttonpow = Button(mframe, text="^", height=1, width=5, command=lambda: press("^"), borderwidth=5, font="bold")
        buttonpsqr = Button(mframe, text="x^2", height=1, width=5, command=lambda: press("s"), borderwidth=5, font="bold")
        buttonpcb = Button(mframe, text="x^3", height=1, width=5, command=lambda: press("c"), borderwidth=5,font="bold")
        buttonpi= Button(mframe, text="π", height=1, width=5, command=lambda: press("π"), borderwidth=5, font="bold")
        buttonsqrt = Button(mframe, text="√", height=1, width=5, command=lambda: press("√"), borderwidth=5, font="bold")
        buttonrt = Button(mframe, text="x√", height=1, width=5, command=lambda: press("r"), borderwidth=5, font="bold")

        button1.grid(row=2, column=2, sticky=W)
        button2.grid(row=2, column=3, sticky=W)
        button3.grid(row=2, column=4, sticky=W)
        button4.grid(row=3, column=2, sticky=W)
        button5.grid(row=3, column=3, sticky=W)
        button6.grid(row=3, column=4, sticky=W)
        button7.grid(row=4, column=2, sticky=W)
        button8.grid(row=4, column=3, sticky=W)
        button9.grid(row=4, column=4, sticky=W)
        button0.grid(row=5, column=2, sticky=W)
        buttonp.grid(row=4,rowspan=3, column=5, sticky=W)
        buttons.grid( row = 6, column = 3,sticky=W)
        buttonm.grid(row=5, column=3, sticky=W)
        buttond.grid(row=5, column=4, sticky=W)
        buttone.grid(row=6, column=4, sticky=W)
        buttonac.grid(row=2, column=5, sticky=W)
        buttonpnt.grid(row=6, column=2, sticky=W)
        buttonc.grid( row=3, column=5,sticky=W)
        buttonb1.grid(row=7, column=2, sticky=W)
        buttonb2.grid(row=7, column=3, sticky=W)
        buttonpow.grid(row=7, column=4, sticky=W)
        buttonpi.grid(row=7, column=5, sticky=W)
        buttonsqrt.grid(row=8, column=2, sticky=W)
        buttonpsqr.grid(row=8, column=3, sticky=W)
        buttonpcb.grid(row=8, column=4, sticky=W)
        buttonrt.grid(row=8, column=5, sticky=W)



root=Tk()
root.title("CALCY")
root.iconbitmap("images.png")
inp = StringVar()
calculator=calc(root,inp)
root.mainloop()

