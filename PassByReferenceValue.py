#!/usr/bin/env python
# coding: utf-8

# In[3]:


def passedBy(a, b):
    # Code here
    a=a+1;
    b=b+2;
    return a,b

a=int(input("a="))
b=int(input("b="))
passedBy(a,b)
print(a,b)
