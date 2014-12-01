class Solution:
	# @return a boolean
	def isValid(self, s):
		if not s:
			return True
		stack = []
		for c in s:
			if c in ["(", "{", "["]:
				stack.append(c)
			elif c == ")":
				if len(stack) == 0 or stack.pop() != "(":
					return False
			elif c == "}":
				if len(stack) == 0 or stack.pop() != "{":
					return False
			elif c == "]":
				if len(stack) == 0 or stack.pop() != "[":
					return False
		if len(stack) != 0:
			return False
		return True

if __name__ == "__main__":
	s = Solution()
	print s.isValid("{([])}")
	print s.isValid("])}")
	print s.isValid("{{{")
