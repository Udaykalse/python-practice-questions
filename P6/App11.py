def p6(b):
    for i in range(1,b+1):
        print(" "*(b-i),end="")
        for j in range(1,i+1):
            print(j,end="")
        for j in range(i-1,0,-1):
            print(j,end="")
        print()

p6(5)