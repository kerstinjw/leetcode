class Solution:
	def lengthOfLastWord(self, s):
		if not s:
			return 0
		length = 0
		for i in range(1,len(s)+1):
			if s[-i] == " ":
				if length > 0: break
				else: continue
			length += 1
		return length

if __name__ == "__main__":
	s = Solution()
	print s.lengthOfLastWord("Hello World!")
	print s.lengthOfLastWord("HelloWorld!")
	print s.lengthOfLastWord("Hello World! ")
	print s.lengthOfLastWord(" ")
