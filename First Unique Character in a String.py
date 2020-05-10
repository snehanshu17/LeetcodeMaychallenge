#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def firstUniqChar(self, s):
        d=set()
        for i in range(len(s)):
            if s[i] not in d :
                d.add(s[i])
            if s.count(s[i])==1:
                return i
        return -1


# In[ ]:




