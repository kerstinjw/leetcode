class Solution:
	def convert(self, s, nRows):
		if nRows == 1:
			return s
		r = 1 
		res = ""
		interval = (nRows - 1)*2
		while r <= nRows:
			i = r - 1 
			while i < len(s):
				res += s[i]
				i += interval
				if r== 1 or r== nRows:
					continue
				if i - (r-1)*2 < len(s):
					res += s[i - r*2 + 2]
			r += 1
		return res

if __name__ == "__main__":
	s = Solution()
	print s.convert("PAYPALISHIRING", 3)
	print s.convert("PAYPALISHIRING", 4)
	print s.convert("PAYPALISHIRING", 5)
