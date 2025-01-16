def getFloorAndCeil(x, arr):
    n=len(arr)
    arr.sort()
    floor=-1
    ceil=-1
        
    for i in range(n):
        if(arr[i]<=x):
            floor=arr[i]
        if(arr[i]>=x and ceil==-1):
            ceil=arr[i]
                
        return [floor,ceil]

arr=[5,6,8,9,6,5,5,6]
x=7
print( getFloorAndCeil(x, arr))
