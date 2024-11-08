def bubbleSort(arr, n):
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            if(arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    return arr

n=int(input("n="))
arr=[]
for i in range(0,n):
    m=int(input())
    arr.append(m)
print(bubbleSort(arr,n))
# print(arr)