class Solution:
	# @param version1, a string
	# @param version2, a string
	# @return an integer
	def compareVersion(self, version1, version2):
		s1 = version1.split(".")
		s2 = version2.split(".")
		for i in range(min(len(s1), len(s2))):
			if int(s1[i]) > int(s2[i]):
				return 1
			if int(s1[i]) < int(s2[i]):
				return -1
		i += 1
		if len(s1) > len(s2):
			while i < len(s1) and int(s1[i]) == 0: i += 1
			if i < len(s1):
				return 1
		else:
			while i < len(s2) and int(s2[i]) == 0: i += 1
			if i < len(s2):
				return -1
		return 0

if __name__ == "__main__":
	s = Solution()
	print s.compareVersion("3.23", "3.4")
	print s.compareVersion("3.4.1", "3.4")
	print s.compareVersion("3.4", "3.4.0.0")
	print s.compareVersion("3.3.1", "3.4")
