class Solution:
	# @return an integer
	def trailingZeroes(self, n):
		res = 0
		tmp = n
		while tmp > 4:
			tmp = tmp / 5
			res += tmp
		return res

if __name__ == "__main__":
	s = Solution()
	print s.trailingZeroes(5)
	print s.trailingZeroes(25)
	print s.trailingZeroes(67)
	print s.trailingZeroes(125)
	print s.trailingZeroes(1024)
