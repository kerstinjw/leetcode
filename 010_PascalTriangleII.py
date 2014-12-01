class Solution:
	# @return a list of integers
	def getRow(self, rowIndex):
		if rowIndex == 0:
			return [1]
		res = [1,1]
		for i in range(1,rowIndex):
			for j in range(0,len(res)-1):
				res[j] = res[j] + res[j+1]
			res.insert(0,1)
		return res

if __name__ == "__main__":
	s = Solution()
	print s.getRow(1)
	print s.getRow(2)
	print s.getRow(3)
	print s.getRow(25)
	print s.getRow(7)
