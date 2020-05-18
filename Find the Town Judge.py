#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust)<N-1:
            return -1
        indegree=[0] * (N+1)
        outdegree=[0] * (N+1)
        
        for out_,in_ in trust :
            
            outdegree[out_]+=1
            indegree[in_]+=1
            
        for i in range(1,N+1):
            if indegree[i]== N-1 and outdegree[i]==0:
                return i
        return -1

