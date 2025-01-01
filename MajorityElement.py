
def majorityElement(nums: list[int]) -> int:
    n=len(nums)
    cnt=0
    el=None

    for i in range(n):
        if cnt==0:
            cnt=1
            el=nums[i]
        elif el==nums[i]:
            cnt+=1
        else:
            cnt-=1
    cnt=0
    for i in range(n):
        if nums[i]==el:
            cnt+=1
    if cnt> (n//2):
        return el
    return -1

nums = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(nums)
print(" Majority element =:", ans)


