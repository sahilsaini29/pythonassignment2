#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[2]:


a=input("enter input word")
print(a[::-1])


# In[ ]:




