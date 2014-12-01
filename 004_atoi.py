#-*- coding:utf-8 -*-
MAX_INT = 2147483647
MIN_INT = -2147483648

class Solution:
	# @return an integer
	def atoi(self, str):
		if not str:
			# null str
			return 0
		index = 0
		mark = 1
		while True:
			if str[index] == " ":
				index += 1
			else:
			 	break
		if str[index] == "-":
			mark = -1
			index += 1
		elif str[index] == "+":
			index += 1
		if ord(str[index]) > ord("9") or ord(str[index]) < ord("0"):
			return 0
		integer = 0
		while index < len(str):
			if ord(str[index]) > ord("9") or ord(str[index]) < ord("0"):
				break
			integer = integer*10 + int(str[index])
			index += 1
		res = integer * mark
		if res > MAX_INT:
			return MAX_INT
		elif res < MIN_INT:
			return MIN_INT
		else:
			return res

if __name__ == "__main__":
	s = Solution()
	print s.atoi("123")
	print s.atoi("-12")
	print s.atoi("#12")
	print s.atoi("1.2")
	print s.atoi("17$12")
	print s.atoi("     12.352")
	print s.atoi("214748321414")
	print s.atoi("-2147483649")
