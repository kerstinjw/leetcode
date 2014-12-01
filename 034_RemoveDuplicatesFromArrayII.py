class Solution:
	def removeDuplicates(self, A):
		if len(A) == 0:
			return 0
		length = 1
		ptr = 1
		flag = 0
		while ptr < len(A):
			if A[length-1] == A[ptr]:
				if flag > 0:
					ptr += 1
					continue
				flag += 1
			else:
				flag = 0
			A[length] = A[ptr]
			length += 1
			ptr += 1
		return length

if __name__ == "__main__":
	s = Solution()
	A = [1,1,1,2,3,44,44,44,79]
	print s.removeDuplicates(A)
	print A
	A = [1,2,3,44,44,44,44,44,44,44,78,78,78,79]
	print s.removeDuplicates(A)
	print A
