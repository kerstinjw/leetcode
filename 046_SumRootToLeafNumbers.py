class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def sumNumbers(self, root):
		if not root:
			return 0
		res = [0] 
		path = ""
		self.DFS(root, path, res)
		return res[0]
	def DFS(self, root, path, res):
		path += str(root.val)
		if not root.left and not root.right:
			res[0] += int(path)
		if root.left:
			self.DFS(root.left, path, res)
		if root.right:
			self.DFS(root.right, path, res)

if __name__ == "__main__":
	a = TreeNode(1)
	b = TreeNode(2)
	c = TreeNode(5)
	d = TreeNode(3)
	e = TreeNode(4)
	a.left = b
	a.right = c
	b.left = d
	b.right = e

	s = Solution()
	print s.sumNumbers(a)
