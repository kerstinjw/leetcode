class Solution:
	def strStr(self, haystack, needle):
		#if not needle:
		#	return 0
		#main = 0
		#sub = 0
		#while main < len(haystack):
		#	if haystack[main] != needle[sub]:
		#		main = main - sub + 1
		#		sub = 0
		#	else:
		#		if sub == len(needle) - 1:
		#			return main - sub
		#		sub += 1
		#		main += 1
		#return -1
		if not needle:
			return 0
		# Build table
		shifts = [1] * (len(needle) + 1)
		shift = 1
		for pos in range(len(needle)):
			while shift <= pos and needle[pos] != needle[pos-shift]:
				shift += shifts[pos-shift]
			shifts[pos+1] = shift
		# Real search	
		index = 0
		match = 0
		while index + match < len(haystack):
			if needle[match] == haystack[index+match]:
				match += 1
				if match == len(needle):
					return index
			else:
				if match == 0:
					index += 1
				else:
					index += shifts[match]
					match -= shifts[match]
		return -1

if __name__ == "__main__":
	s = Solution()
	print s.strStr("mississippi", "ABCDABD")
	print s.strStr("mississippi", "pi")
