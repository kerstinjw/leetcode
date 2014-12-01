#-*- coding:utf-8 -*-

class Solution:
	# @return an integer
	def reverse(self, x):
		y = 0
		mark = 1
		if x < 0:
			mark = -1
		ori = x * mark
		tmp = 0
		while ori>0:
			tmp = ori%10
			y = y*10 + tmp
			ori = ori/10
		return y*mark

if __name__ == "__main__":
	s = Solution()
	print s.reverse(10000000)
	print s.reverse(-21314)
	print s.reverse(999992190214)
