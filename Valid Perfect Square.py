#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, high = 1, num
        while low <= high:
            mid = low + (high-low)//2
            sq = mid*mid
            if sq == num:
                return True
            elif sq > num:
                high = mid - 1
            else:
                low = mid + 1
        return False


# In[ ]:




