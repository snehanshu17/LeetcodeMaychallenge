#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(num)[len(num)/2]


# In[ ]:


class Solution(object):
    def majorityElement(self, nums):
        count=0
        candidate=None
        for num  in nums:
            if count==0:
                candidate num 
            count+=1=(1 if num==candidate else -1)

