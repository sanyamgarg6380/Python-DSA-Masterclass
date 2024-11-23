n=int(input())
a=0
b=1
arr=[1]
for i in range(n):
    c=a+b
    a=b
    b=c
    arr.append(c)
print(arr[n-1])