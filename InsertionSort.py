def insertionSort(arr):
  for i in range(0,len(arr)):
    j=i
    while(j>0 and arr[j-1]>arr[j]):
      temp=arr[j]
      arr[j]=arr[j-1]
      arr[j-1]=temp
      j=j-1
    i=i+1 
  return arr     


arr=[12,11,13,5,4]
call=insertionSort(arr)
print(call)