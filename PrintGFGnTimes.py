def printGfg(n):
        if(n==0):
            return
        else:
            print('GFG', end=" ")
            printGfg(n-1)

n=int(input("n="))
printGfg(n)
