#-*- coding:utf-8 -*-

class Solution:
	# @return a boolean
	def isPalindrome(self, x):
		if x < 0:
			return False
		len = 0
		ori = x
		while ori > 0:
			len += 1
			ori = ori/10
		i = 0
		former = pow(10,len-1)
		latter = 10
		while i < (len+1)/2:
			if ((x/former)%10) ^ ((x%latter)/pow(10,i)):
				return False
			former = former / 10
			latter = latter * 10
			i += 1
		return True

if __name__ == "__main__":
	s = Solution()
	print s.isPalindrome(12345)
	print s.isPalindrome(123321)
	print s.isPalindrome(-121)
	print s.isPalindrome(0)
	print s.isPalindrome(1)
	print s.isPalindrome(-1)

