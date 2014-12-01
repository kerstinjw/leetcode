#-*- coding:utf-8 -*-

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def isSymmetric(self, root):
		if not root:
			return True
		if not root.left and not root.right:
			return True
		if not root.left and root.right:
			return False
		if root.left and not root.right:
			return False

		lstack = []
		rstack = []
		lstack.append(root.left)
		rstack.append(root.right)
		while len(lstack)>0 and len(rstack)>0:
			lcur = lstack.pop(0)
			rcur = rstack.pop(0)
			if not lcur and not rcur:
				continue
			if not lcur or not rcur:
				return False
			if lcur.val != rcur.val:
				return False
			lstack.append(lcur.left)
			lstack.append(lcur.right)
			rstack.append(rcur.right)
			rstack.append(rcur.left)
		if len(lstack) != len(rstack):
			return False
		return True
		

if __name__ == "__main__":
	nodeA = TreeNode("1")
	nodeB = TreeNode("2")
	nodeC = TreeNode("2")
	nodeD = TreeNode("3")
	nodeE = TreeNode("3")
	nodeF = TreeNode("2")
	nodeG = TreeNode("2")
	nodeA.left = nodeB
	nodeA.right = nodeC
	nodeB.right = nodeD
	nodeC.right = nodeE
	#nodeD.left = nodeF
	#nodeE.left = nodeG

	s = Solution()
	print s.isSymmetric(nodeA)
