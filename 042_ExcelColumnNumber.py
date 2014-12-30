class Solution:
	# @param s, a string
	# @return an integer
	def titleToNumber(self, s):
		res = 0
		for i in range(len(s)):
			res = res*26 + ord(s[i]) - 64
		return res

if __name__ == "__main__":
	s = Solution()
	print s.titleToNumber("A")
	print s.titleToNumber("Z")
	print s.titleToNumber("AB")
	print s.titleToNumber("AZ")
