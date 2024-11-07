 def getSecondLargest(arr):
        largest=0
        s_largest=0
        count = 0
        if len(arr)==0 or len(arr)==1:
            s_largest=-1
        else:
            for i in range(len(arr)):
                if arr[i]>largest:
                    largest = arr[i]
                    count = i
                arr[count] = -1 
            for i in range(len(arr)):
                if arr[i]>s_largest:
                    s_largest = arr[i]
        return s_largest


arr=[]
n=int(input("n="))
for i in range(0,n):
    v=int(input())
    arr.append(v)
print(getSecondLargest(arr))