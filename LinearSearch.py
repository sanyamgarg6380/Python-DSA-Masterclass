def searchInSorted(self,arr, k):
        for i in range(0,len(arr)):
            if(arr[i]==k):
                return True 
            else:
                return False

arr=[]
k=int(input("k="))
n=int(input("n="))
for i in range(0,n):
    v=int(input())
    arr.append(v)
print(searchInSorted(arr))