class Solution:
	def addBinary(self, a, b):
		if len(a) > len(b):
			b = "0"*(len(a)-len(b)) + b
		else:
			a = "0"*(len(b)-len(a)) + a
		carry = 0
		res = ""
		for i in range(1, len(a)+1):
			digit = ( int(a[-i]) ^ int(b[-i]) ) ^ carry
			if int(a[-i]) + int(b[-i]) + carry >= 2:
				carry = 1
			else:
				carry = 0
			res = "%d%s" % (digit, res)
		if carry == 1:
			res = "1" + res
		return res

if __name__ == "__main__":
	s = Solution()
	print s.addBinary("1111", "10")
	print s.addBinary("1111", "1110")
	print s.addBinary("1001", "101")

