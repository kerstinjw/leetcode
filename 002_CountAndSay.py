#-*- coding:utf-8 -*-

class Solution:
	# @return a string
	def countAndSay(self, n):
		former = "1"
		latter = ""
		counter = n
		while counter>1:
			cur = former[0]
			cnt = 1
			for i in range(1,len(former)):
				if cur == former[i]:
					cnt +=1
				else:
					latter += "%d%s" % (cnt, cur)
					cur = former[i]
					cnt = 1
			latter += "%d%s" % (cnt, cur)
			former = latter
			latter = ""
			counter = counter - 1
		return former

if __name__ == "__main__":
	s = Solution()
	print s.countAndSay(1)
	print s.countAndSay(2)
	print s.countAndSay(3)
	print s.countAndSay(4)
	print s.countAndSay(5)
	print s.countAndSay(6)
	print s.countAndSay(7)
	print s.countAndSay(8)
	print s.countAndSay(9)

