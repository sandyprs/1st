import random
import string


def cb(ch,cch):

    cow=0
    bull=0

    for i in range(4):
        for j in range(4):
            if cch[i]==ch[j] and i==j:
                cow+=1
            elif cch[i]==ch[j]:
                bull+=1
            else:
                continue
    return cow,bull


if __name__=="__main__":
    ch = input("enter a four digit number:: ")
    cch = random.randint(1000, 9999)
    print(cch)
    cchs = str(cch)
    while ch!='x':

        cow,bull=cb(ch,cchs)
        print('you have got ',cow,'cows and ',bull ,'bulls')
        ch = input("enter a four digit number:: ")
