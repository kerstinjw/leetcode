class Solution:
	def convertToTitle(self, num):
		res = ""
		tmp = num - 1
		while tmp > -1:
			res = chr(tmp%26+65) + res
			tmp = tmp/26 - 1
		return res

if __name__ == "__main__":
	s = Solution()
	print s.convertToTitle(26)
	print s.convertToTitle(1)
	print s.convertToTitle(28)
	print s.convertToTitle(128)
