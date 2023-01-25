#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=int(input())
b=int(input())
x=bin(a)[2:]
print(x)
y=bin(b)[2:]
print(y)
def ones_complement(s):
    res=""
    for i in s:
        if i=='0':
            res += '1'
        else:
            res += '0'
    return res
x=ones_complement(x)
print(x)
y=ones_complement(y)
print(y)
print(int(x,2)^int(y,2))


# In[ ]:




