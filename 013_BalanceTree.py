class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def isBalanced(self, root):
		if not root:
			return True
		tmp = self.maxDepth(root.left) - self.maxDepth(root.right)
		if tmp > 1 or tmp < -1:
			return False
		return self.isBalanced(root.left) and self.isBalanced(root.right)
	def maxDepth(self, node):
		if not node:
			return 0
		return max(self.maxDepth(node.left), self.maxDepth(node.right)) + 1

if __name__ == "__main__":
	a = TreeNode(5)
	b = TreeNode(4)
	c = TreeNode(8)
	d = TreeNode(11)
	e = TreeNode(13)
	f = TreeNode(4)
	g = TreeNode(7)
	h = TreeNode(2)
	i = TreeNode(1)
	a.left = b
	a.right = c
	b.left = d
	c.right = e
	d.left = f
	e.right = g
	f.left = h
	g.right = i

	s = Solution()
	print s.isBalanced(a)
	print s.isBalanced(b)
