#!/usr/bin/env python
# coding: utf-8

# # FIRST BAD VERSION 

# In[1]:


class Solution :
    def firstBadVersion(self,n):
        start=1
        end=n
        
        while start<end :
            mid=(start+end)//2
            if isBadVersion(mid):
                end=mid
            else:
                start=mid+1
            return start


# In[ ]:




