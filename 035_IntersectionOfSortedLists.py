class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param two ListNodes
	# @return the intersected ListNode
	def getIntersectionNode(self, headA, headB):
		if headA is None or headB is None:
			return None
		pA = headA
		pB = headB
		while True:
			if pA.val == pB.val:
				return pA
			pA = pA.next
			pB = pB.next
			if pA is None and pB is None:
				return None
			if pA is None and pB is not None:
				pA = headB
			if pA is not None and pB is None:
				pB = headA

if __name__ == "__main__":
	a = ListNode(1)	
	b = ListNode(2)	
	c = ListNode(3)	
	d = ListNode(4)	
	e = ListNode(5)	
	f = ListNode(6)	
	g = ListNode(7)	
	a.next = b
	b.next = c
	c.next = d
	d.next = f
	f.next = g
	e.next = d

	s = Solution()
	print s.getIntersectionNode(g, e).val
