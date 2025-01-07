def findFloor(arr,k):
    n=len(arr)
    low=0
    high=n-1
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]<=k):
            ans=mid
            low = mid+1
        else:
            high=mid-1
    return ans

arr=[1,2,8,10,11,12,19]
print(findFloor(arr,0))