def sumOfDivisors( N):
        ans=0
        for i in range(1,N+1):
             ans += i * (N // i)
        return ans

N=int(input("N="))
print(sumOfDivisors(N))