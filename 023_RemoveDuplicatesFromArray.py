class Solution:
	def removeDuplicates(self, A):
		if len(A) == 0:
			return 0
		length = 1
		index = 1
		val = A[0]
		while index < len(A):
			if A[index] != val:
				A[length] = A[index]
				val = A[index]
				length += 1
			index += 1
		return length

if __name__ == "__main__":
	s = Solution()
	A = [1,1]
	res = s.removeDuplicates(A)
	print A, res
	A = [1,1,2,3]
	res = s.removeDuplicates(A)
	print A, res
