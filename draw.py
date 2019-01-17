def draw(n):
    dash='...'
    pip='|'
    for i in range(n):
        print(' ...',end='')
    print()

    for i in range(n):
        print(pip, end="")
        for j in range(n):
            print(dash,end="")
            print(pip,end="")
        print()



if __name__=="__main__":
    n=int(input("enter limit:: "))
    draw(n)