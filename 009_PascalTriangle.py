class Solution:
	# @return a list of lists of integers
	def generate(self, numRows):
		triangle = []
		line = [1]
		for num in range(0,numRows):
			triangle.append(line)
			tmp = [1]
			for i in range(0,len(line)-1):
				tmp.append(line[i]+line[i+1])
			tmp.append(1)
			line = tmp
		return triangle

if __name__ == "__main__":
	s = Solution()
	#print s.generate(1)
	#print s.generate(2)
	print s.generate(5)
	#print s.generate(10)
