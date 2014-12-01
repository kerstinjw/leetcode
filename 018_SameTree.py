class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isSameTree(self, p, q):
		if not p and not q:
			return True
		if not p or not q:
			return False
		if p.val != q.val:
			return False
		queue_p = [p]
		queue_q = [q]
		while len(queue_p) > 0 and len(queue_q) > 0:
			cur_p = queue_p.pop(0)
			cur_q = queue_q.pop(0)
			if cur_p.left and cur_q.left:
				if cur_p.left.val != cur_q.left.val:
					print 1
					return False
				queue_p.append(cur_p.left)
				queue_q.append(cur_q.left)
			elif cur_p.left and not cur_q.left:
				print 2
				return False
			elif not cur_p.left and cur_q.left:
				print 3
				return False
			if cur_p.right and cur_q.right:
				if cur_p.right.val != cur_q.right.val:
					print 4
					return False
				queue_p.append(cur_p.right)
				queue_q.append(cur_q.right)
			elif cur_p.right and not cur_q.right:
				print 5
				return False
			elif not cur_p.right and cur_q.right:
				print 6
				return False
		if len(queue_p) > 0 or len(queue_q) >0:
			return False
		return True

if __name__ == "__main__":
	a = TreeNode(1)
	b = TreeNode(2)
	a.right = b
	c = TreeNode(1)
	d = TreeNode(2)
	c.right = d

	s = Solution()
	print s.isSameTree(a,c)
