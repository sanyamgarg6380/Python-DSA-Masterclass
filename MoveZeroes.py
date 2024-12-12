def moveZeroes(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        if(nums[i]!=0):
            i+=1
        n=len(nums)
        if(n>1):
            for j in range(1,n):
                if(nums[j]!=0):
                    nums[i]=nums[j]
                    i+=1
                
            for k in range(i,n):
                nums[k]=0

arr=[]
n=int(input("n="))
for i in range(0,n):
    v=int(input())
    arr.append(v)
print(moveZeroes(arr))

