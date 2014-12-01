class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @return a ListNode
	def removeNthFromEnd(self, head, n):
		if head is None:
			return []
		latter = head
		for i in range(0,n):
			latter = latter.next
		if latter is None:
			tmp = head.next
			del head
			return tmp
		former = head
		while latter.next:
			former = former.next
			latter = latter.next
		tmp = former.next
		former.next = tmp.next
		del tmp
		return head

if __name__ == "__main__":
	a = ListNode(1)
	b = ListNode(2)
	c = ListNode(3)
	d = ListNode(4)
	e = ListNode(5)
	a.next = b
	b.next = c
	c.next = d
	d.next = e

	s = Solution()
	cur = s.removeNthFromEnd(d, 2)
	while cur:
		print cur.val
		cur = cur.next
