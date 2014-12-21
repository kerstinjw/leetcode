class Solution:
	def threeSum(self, num):
		num.sort()
		res = []
		for i in range(0,len(num)-2):
			if i > 0 and num[i] == num[i-1]:
				continue
			a = num[i]
			start = i + 1
			end = len(num) - 1
			while start < end:
				b = num[start]
				c = num[end]
				if a+b+c == 0:
					res.append([a,b,c])
					end -= 1
					start += 1
					while start < end and num[start] == num[start-1]: start += 1
					while start < end and num[end] == num[end+1]: end -= 1
				elif a+b+c > 0:
					end -= 1
					while start < end and num[end] == num[end+1]: end -= 1
				else:
					start += 1
					while start < end and num[start] == num[start-1]: start += 1
		return res


if __name__ == "__main__":
	s = Solution()
	print s.threeSum([-1, 0, 1, 2, -1, -4])
	print s.threeSum([0, 0, 0, 0])
	print s.threeSum([3,0,-2,-1,1,2])
	#print s.threeSum([7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6])
