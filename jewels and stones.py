#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels_set=set([i for i in J])
        ret=0
        
        for i in S:
            if i in jewels_set:
                ret+=1
        return ret

