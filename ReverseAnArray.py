def reverseArray(arr):
    i=0
    j=len(arr)-1
    while i<j:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=1
        j-=1
    return arr

arr=[1,2,3,4]
print(reverseArray(arr))
