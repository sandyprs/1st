
print("player 1 gets 'x' & \nplayer 2 gets 'o'")
print("please give the position separated by ','(comma)")
lst1=[0,0,0]
lst2=[0,0,0]
lst3=[0,0,0]
mat=[lst1,lst2,lst3]
def winner(player):
    if player=='x':
        print("the winner is player 1")
        return True
    elif player=='o':
        print("the winner is player 2")
        return True
    else:
        return False



def wincheck():
    wn=False
    gameover=False
    while gameover==False:
        if lst1[0] == lst1[1] == lst1[2]:
                wn=winner(lst1[0])
                gameover = True
                break
        if lst2[0] == lst2[1] == lst2[2]:
                wn=winner(lst2[0])
                gameover = True
                break
        if lst3[0] == lst3[1] == lst3[2]:
                wn=winner(lst3[0])
                gameover = True
                break
        if lst1[0] == lst2[0] == lst3[0]:
                wn=winner(lst3[0])
                gameover = True
                break
        if lst1[1] == lst2[1] == lst3[1]:
                wn=winner(lst3[1])
                gameover = True
                break
        if lst1[2] == lst2[2] == lst3[2]:
                wn=winner(lst3[2])
                gameover = True
                break
        if lst1[0] == lst2[1] == lst3[2]:
                wn=winner(lst1[0])
                gameover = True
                break
        if lst1[2] == lst2[1] == lst3[0]:
                wn=winner(lst3[0])
                gameover = True
                break
        else:
            fg = False
            for j in mat:
                for k in j:
                    if k != 0:
                        fg = True
                    else:
                        fg = False
                        break
            if fg == True:
                print("game dismissed!!")
            gameover = True
            break


    return wn


if __name__=="__main__":
    for i in range(5):
        while True:
            p = input("player1:: ")
            p = p.split(",")
            x = int(p[0]) - 1
            y = int(p[1]) - 1
            if mat[x][y] == 0:
                mat[x][y] = "x"
                break
            else:
                print("try again!!\n")
        wn = wincheck()
        for j in mat:
            print(j)
        print()
        if wn == True:
            break


        if i==4:
            break
        else:
            while True:
                p = input("player2:: ")
                p = p.split(",")
                x = int(p[0]) - 1
                y = int(p[1]) - 1
                if mat[x][y] == 0:
                    mat[x][y] = "o"
                    break
                else:
                    print("try again!!\n")
            wn = wincheck()
            for i in mat:
                print(i)
            print()
            if wn == True:
                break

