#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def findComplement(self, num):
        str=['1'  if i=='0' else '0' for i in bin(num)[2:]]
        return int(''.join(str), 2)
                
        


# In[ ]:




