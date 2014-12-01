class Solution:
	def climbStairs(self, n):
		if n == 1:
			return 1
		if n == 2:
			return 2
		f_n1 = 1
		f_n2 = 2
		for i in range(3,n+1):
			f_n = f_n1 + f_n2
			f_n1 = f_n2
			f_n2 = f_n
		return f_n

if __name__ == "__main__":
	s = Solution()
	print s.climbStairs(3)
	print s.climbStairs(1)
	print s.climbStairs(2)
	print s.climbStairs(19)
