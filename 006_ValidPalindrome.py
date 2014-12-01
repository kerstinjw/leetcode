#-*- coding:utf-8 -*-
class Solution:
	# @param s, a string
	# @return a boolean
	def isPalindrome(self, s):
		if not s:
			return True
		sp = 0
		ep = len(s) - 1
		while sp < ep:
			while sp < ep:
				if ord(s[sp].lower()) >= ord("a") and ord(s[sp].lower()) <= ord("z"):
					break
				if ord(s[sp]) >= ord("0") and ord(s[sp]) <= ord("9"):
					break
				sp += 1
			while sp < ep:
				if ord(s[ep].lower()) >= ord("a") and ord(s[ep].lower()) <= ord("z"):
					break
				if ord(s[ep]) >= ord("0") and ord(s[ep]) <= ord("9"):
					break
				ep -= 1
			if s[sp].lower() != s[ep].lower():
				return False
			sp += 1
			ep -= 1
		return True

if __name__ == "__main__":
	s = Solution()
	print s.isPalindrome("A man, a plan, a canal: Panama")
	print s.isPalindrome("a   b,321,ba")
	print s.isPalindrome("race a car")
	print s.isPalindrome("3432")
	print s.isPalindrome("1a2")
	print s.isPalindrome(",#")
	print s.isPalindrome("ab")
