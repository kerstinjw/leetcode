# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	#@return a ListNode
	def addTwoNumbers(self, l1, l2):
		p1 = l1
		p2 = l2
		up = (p1.val + p2.val)/10
		head = ListNode((p1.val + p2.val)%10)
		p = head
		while p1.next and p2.next:
			p1 = p1.next
			p2 = p2.next
			p.next = ListNode((p1.val + p2.val + up) % 10)
			p = p.next
			up = (p1.val + p2.val + up) / 10
		if p1.next:
			tmp = p1.next
		else:
			tmp = p2.next
		while tmp:
			p.next = ListNode((tmp.val + up) % 10)
			up = (tmp.val + up) / 10
			p = p.next
			tmp = tmp.next
		if up > 0:
			p.next = ListNode( up )
		return head

if __name__ == "__main__":
	a = ListNode(0)
	b = ListNode(4)
	c = ListNode(5)
	a.next = b
	b.next = c

	d = ListNode(0)
	e = ListNode(6)
	f = ListNode(4)
	g = ListNode(9)
	h = ListNode(9)
	i = ListNode(9)
	j = ListNode(9)
	d.next = e
	e.next = f
	f.next = g
	g.next = h
	h.next = i
	i.next = j

	s = Solution()
	res = s.addTwoNumbers(a,d)
	while res:
		print res.val
		res = res.next
