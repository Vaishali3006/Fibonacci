#!/usr/bin/env python
# coding: utf-8

# In[11]:


#fibonacci series
n3=0
n1=0
n2=1
i=0

while i<20:  
    """for infinite values write while i>0"""
    if i<=1:
        n3=i
    else:
        n3=n1+n2
        n1=n2
        n2=n3
    print(n3)
    i+=1
print("end of range")






