def printNos(N):
        if(N==0):
            return
        printNos(N-1)
        print(N, end=" ")

N=int(input("N="))
printNos(N)