def transpose(l):

    trans=[]
    j=0
    for i in range(0,len(l[j])):
        tps = []
        for row in l:
            tps.append(row[i])
        trans.append(tps)


    return trans




k=transpose([[1,2,7],[4,5,8],[8,9,4]])
print(k)