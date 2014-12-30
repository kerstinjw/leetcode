class Solution:
	# @param s, a string
	# @return a list of lists of string
	def partition(self, s):
		res = []
		layer = []
		self.DFS(s, 0, layer, res)
		return res
	def DFS(self, s, start, layer, res):
		if start == len(s):
			res.append(list(layer))
			return
		for i in range(start,len(s)):
			if self.isPalidrome(s, start, i):
				layer.append(s[start:i+1])
				self.DFS(s, i+1, layer, res)
				layer.pop()
	def isPalidrome(self, s, start, end):
		while start < end:
			if s[start] != s[end]:
				return False
			start += 1
			end -= 1
		return True

if __name__ == "__main__":
	s = Solution()
	print s.partition("efe")
	print s.partition("aabcdbdcc")
	print s.partition("aabcc")
