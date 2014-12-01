class Solution:
	# @param A  a list of integers
	# @param m  an integer, length of A
	# @param B  a list of integers
	# @param n  an integer, length of B
	# @return nothing
	def merge(self, A, m, B, n):
		if m == 0:
			A += B
		if n == 0:
			return
		i = m - 1
		j = n - 1
		k = m + n - 1
		while i >=0 and j >= 0:
			if A[i] < B[j]:
				A[k] = B[j]
				j -= 1
			else:
				A[k] = A[i]
				i -= 1
			k -= 1
		while j >= 0:
			A[j] = B[j]
			j -= 1

if __name__ == "__main__":
	A = [12,33,56,0]
	B = [1]
	
	s = Solution()
	s.merge(A, 3, B, 1)
	print A
