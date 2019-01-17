import random
from time import sleep
def guess():
    count=0
    a=random.randint(1,25)
    b=int(input ("guess the number "))
    if a==b:
        print("yheee!! you have done good job")
        count=1
    elif a>b:
        print("aha!! you are too low")
        print("the number was ",a)
    else:
        print("oh no!! you are too high")
        print("the number was ", a)
    return count


ch='o'
counter = 0
count=0
while ch!='x':
    counter+=1
    count+=guess()
    ch=input("to exit enter 'x' else press any key ")
print("you have guessed",count,"out of",counter)
sleep(2)