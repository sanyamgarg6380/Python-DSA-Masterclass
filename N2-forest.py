def n2Forest(n) ->None:
    for i in range(0,n):
        for j in range(0,i+1):
            print("*", end=" ")
        print()

n=int(input("n="))
print(n2Forest(n))