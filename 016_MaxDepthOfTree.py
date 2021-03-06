class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def maxDepth(self, root):
		if not root:
			return 0
		depth = 0
		queue = [root]
		last = 1
		count = 0
		while len(queue) > 0:
			cur = queue.pop(0)
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
		return depth

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
	print s.maxDepth(a)
