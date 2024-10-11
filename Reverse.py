#!/usr/bin/env python
# coding: utf-8

# In[10]:


def reverse(x):
    reverse=0
    isNegative=False

    if x<0:
        isNegative=True
        x=-x

    while x>0:   
        lastDigit=x%10
        reverse=(reverse*10)+lastDigit
        x=x//10

    if isNegative==True:
        reverse=-reverse

    if reverse<-2**31 or reverse> 2**31-1:
        return 0

    return reverse


x=int(input("x="))
reverse(x)

