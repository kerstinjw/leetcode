class Solution:
	def plusOne(self, digits):
		res = []
		carry = 1
		for i in range(1,len(digits)+1):
			tmp = ( digits[-i] + carry ) % 10
			if tmp == 0 and carry == 1:
				carry = 1
			else:
				carry = 0
			res.insert(0, tmp)
		if carry == 1:
			res.insert(0, 1)
		return res

if __name__ == "__main__":
	s = Solution()
	print s.plusOne([1,9,2,4,9])
	print s.plusOne([1,9,9,9,9])
	print s.plusOne([9,9])
