class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def minDepth(self, root):
		#if not root:
		#	return 0
		#if not root.left and not root.right:
		#	return 1
		#if not root.left and root.right:
		#	return self.minDepth(root.right) + 1
		#if root.left and not root.right:
		#	return self.minDepth(root.left) + 1
		#return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
		if not root:
			return 0
		queue = [root]
		depth = 1
		count = 0
		last = 1
		while len(queue) > 0:
			cur = queue.pop(0)
			if not cur.left and not cur.right:
				return depth
			last -= 1
			if cur.left:
				queue.append(cur.left)
				count += 1
			if cur.right:
				queue.append(cur.right)
				count += 1
			if last == 0:
				depth += 1
				last = count
				count = 0

if __name__ == "__main__":
	a = TreeNode(1)
	b = TreeNode(2)
	c = TreeNode(3)
	d = TreeNode(4)
	e = TreeNode(5)
	f = TreeNode(6)
	g = TreeNode(7)
	h = TreeNode(8)
	i = TreeNode(9)
	a.left = b
	a.right = c
	b.left = d
	c.left = e
	c.right = f
	d.left = g
	d.right = h
	f.right = i

	s = Solution()
	print s.minDepth(a)
