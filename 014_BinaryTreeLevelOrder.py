class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def levelOrder(self, root):
		if not root:
			return []
		tree = []
		last = 1
		count = 0
		queue = [root]
		level = []
		while len(queue) > 0:
			cur = queue.pop(0)
			level.append(cur.val)
			last -= 1
			if cur.left:
				count += 1
				queue.append(cur.left)
			if cur.right:
				count += 1
				queue.append(cur.right)
			if last == 0:
				tree.append(level)
				level = []
				last = count
				count = 0
		return tree

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
	print s.levelOrder(a)
