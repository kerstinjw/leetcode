class Solution:
	# @param num, a list of integers
	# @return an integer
	def majorityElement(self, num):
		if len(num) == 1:
			return num[0]
		# Answer 1 - O(nlogn)
		#num.sort()
		#middle = len(num)/2
		#return num[middle]
		# Answer 2 (Moore Voting Algorithm) - O(n)
		count = 0
		for i in range(0,len(num)):
			if count == 0:
				voting = num[i]
				count = 1
			else:
				if voting == num[i]:
					count += 1
				else:
					count -= 1
		return voting
		

if __name__ == "__main__":
	s = Solution()
	print s.majorityElement([1,3,1,4,1])
	print s.majorityElement([3,1,5,1])
