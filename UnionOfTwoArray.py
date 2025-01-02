def findUnion(a,b):
    union=list(set(a+b))
    union.sort()
    return union
a=[2,2,3,4,5]
b=[1,1,2,3,4]
print(findUnion(a,b))