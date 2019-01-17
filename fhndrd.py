import random

cont=[]
for i in range(500):
    cont.append(random.randint(1,1000))
with open("fndrd.txt","w") as fl1:
    for i in cont:
        fl1.writelines(str(i)+" ")

fl1.close()

