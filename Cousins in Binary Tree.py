#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
	def isCousins(self, root, x, y):
		"""
		:type root: TreeNode
		:type x: int
		:type y: int
		:rtype: bool
		"""
		res = []
		self.help(root, x, y, 0, res, None)
		if res[0][0] == res[1][0] and res[0][1] != res[1][1]: return True
		return False

	def help(self, root, x, y, depth, res, parent):
		if root == None: return 
		if root.val == x:res.append((depth, parent))
		if root.val == y: res.append((depth, parent))
		self.help(root.left, x, y, depth + 1, res, root)
		self.help(root.right, x, y, depth + 1, res, root)


# In[ ]:




