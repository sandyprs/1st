def valley(l):
    c=False
    j=0
    if l[0] == 1:
        return c
    if l[0] >1:
        while l[j]!=1:
            if l[j]>l[j+1]:
                c=True
            else:
                c = False
                break
            j+=1
    else:
        return c

    if l[j]==1:
        for j in range(j, len(l) - 1):
            if l[j] < l[j + 1]:
                c = True
            else:
                c=False
                break
    return c


k=valley([3])

print(k)