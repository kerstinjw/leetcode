class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def deleteDuplicates(self, head):
		if not head:
			return head
		node = head
		val = head.val
		while node.next:
			if node.next.val == val:
				tmp = node.next
				node.next = tmp.next
				del tmp
			else:
				node = node.next
				val = node.val
		return head

if __name__ == "__main__":
	a = ListNode(1)
	b = ListNode(2)
	c = ListNode(2)
	d = ListNode(6)
	e = ListNode(6)

	a.next = b
	b.next = c
	c.next = d
	d.next = e

	s = Solution()
	res = s.deleteDuplicates(a)
	while res:
		print res.val
		res = res.next
