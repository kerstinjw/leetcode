class Solution:
	def removeElement(self, A, elem):
		if not A:
			return 0
		length = 0
		index = 0
		while index < len(A):
			if A[index] != elem:
				A[length] = A[index]
				length += 1
			index += 1
		return length

if __name__ == "__main__":
	s = Solution()
	A = [1]
	print s.removeElement(A,2), A
	A = [1,2,3,4,6,6]
	print s.removeElement(A,4), A
	A = [1,2,3,4,6,6]
	print s.removeElement(A,6), A
