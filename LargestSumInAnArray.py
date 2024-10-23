def largest(arr):
    largest=0
    for i in range(0,len(arr)):
        if(arr[i]>largest):
            largest=arr[i]
    return largest

arr=[]
n=int(input("n="))
for i in range(0,n):
    v=int(input())
    arr.append(v)
print(largest(arr))