#-*- coding:utf-8 -*-
class Solution:
	# @return a string
	def longestCommonPrefix(self, strs):
		if not strs:
			return ""
		max = 0
		res = ""
		while max < min([len(s) for s in strs]):
			tmp = strs[0][max]
			for s in strs:
				if tmp != s[max]:
					return res
			res += tmp
			max += 1
		return res

if __name__ == "__main__":
	s = Solution()
	print s.longestCommonPrefix(["ab", "ac", "abc"])
	print s.longestCommonPrefix(["8989", "8919", "89"])
	print s.longestCommonPrefix(["1", "#", ""])
