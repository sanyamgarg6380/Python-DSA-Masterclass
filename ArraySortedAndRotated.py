def check( nums: list[int]) -> bool:
  count=0
  n=len(nums)
  for i in range(n):
    if nums[i] > nums[(i+1) % n]:
      count+=1
  if(count>1):
    return False
  else:
    return True

nums=[]
value=int(input())
for i in range(value):
  c=input()
  nums.append(c)
print(check(nums))

