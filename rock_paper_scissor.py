import getpass



def game(plr1,plr2):
    if plr1=='rock' and plr2=='paper' or plr1=='paper' and plr2=='scissor' or plr1 == 'scissor' and plr2 == 'rock':
        print('congratulations!!! winner is player2')
    elif plr1=='rock' and plr2=='scissor' or plr1=='paper' and plr2=='rock' or  plr1 == 'scissor' and plr2 == 'paper':
        print('congratulations!!! winner is player1')
    else:
        print("game dismissed")

p='k'
while(p!='x'):
    plr1=getpass.getpass("turn of player1 ")
    plr2=getpass.getpass("turn of player2 ")
    game(plr1,plr2)
    print("player 1 choose "+plr1)
    print("player 2 choose "+plr2)
    p=input("to exit enter 'x'")