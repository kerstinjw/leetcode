class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def mergeTwoLists(self, l1, l2):
		if not l1 and not l2:
			return None
		if not l1 and l2:
			return l2
		if l1 and not l2:
			return l1
		if l1.val < l2.val:
			p1 = l1
			p2 = l2
			head = l1
		else:
			p1 = l2
			p2 = l1
			head = l2
		while p1.next is not None and p2 is not None:
			if p1.next.val > p2.val:
				tmp = p2.next
				p2.next = p1.next
				p1.next = p2
				p1 = p2
				p2 = tmp
			else:
				p1 = p1.next
		if p2 is not None:
			p1.next = p2
		return head

if __name__ == "__main__":
	a = ListNode(1)
	b = ListNode(3)
	c = ListNode(5)
	d = ListNode(2)
	e = ListNode(4)
	f = ListNode(6)
	g = ListNode(10)
	h = ListNode(11)
	a.next = b
	b.next = c
	d.next = e
	e.next = f
	f.next = g
	c.next = h

	s = Solution()
	head = s.mergeTwoLists(a, d)
	while head is not None:
		print head.val
		head = head.next
