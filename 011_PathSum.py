class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def DLR(self, root):
		stack = []
		res = []
		s = [0]
		cur = root
		while cur or len(stack) > 0:
			res.append(cur.val)
			s[-1] += cur.val	
			while cur.left:
				stack.append(cur)
				cur = cur.left
				res.append(cur.val)
				s[-1] += cur.val
			if not cur.right:
				s.append( s[-1] - cur.val )
			cur = cur.right
			former = 0
			while not cur and len(stack) > 0:
				#cur = stack.pop().right
				tmp = stack.pop()
				s[-1] -= former
				former = tmp.val
				cur = tmp.right
		print s
		return res
	def hasPathSum(self, root, sum):
		# Recursive
		#if not root:
		#	return False
		#if sum < root.val:
		#	return False
		#if not root.left and not root.right:
		#	if sum == root.val:
		#		return True
		#	else:
		#		return False
		#res = False
		#if root.left:
		#	res = res or (self.hasPathSum(root.left, sum-root.val))
		#if root.right:
		#	res = res or (self.hasPathSum(root.right, sum-root.val))
		#return res
		# ----- None Recursive -----
		pass

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
	c.left = e
	c.right = f
	d.left = g
	d.right = h
	f.right = i

	s = Solution()
	print s.DLR(a)
