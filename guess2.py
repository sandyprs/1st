import random
low=0
high=100
search='no'
myno=int(input("enter your choice:: "))
cguess = 50
print(cguess)
search = input()
while search=='no':
   if cguess>myno:
       cguess=(cguess+low)/2
       low=cguess
   elif cguess<myno:
       cguess=(cguess+high)/2
       high=

