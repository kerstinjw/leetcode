class Solution:
	def threeSumClosest(self, num, target):
		num.sort()
		mindiff = 2147483647
		for i in range(0,len(num)-2):
			if i > 0 and num[i] == num[i-1]:
				continue
			start = i + 1
			end = len(num) - 1
			while start < end:
				s = num[i] + num[start] + num[end]
				diff = abs(s-target)
				if diff < mindiff:
					mindiff = diff
					res = s
					if s == target:
						return s
				if s > target:
					end -= 1
					while start < end and num[end] == num[end+1]: end -= 1
				else:
					start += 1
					while start < end and num[start] == num[start-1]: start += 1
		return res

if __name__ == "__main__":
	s = Solution()
	print s.threeSumClosest([-1,2,1,-4], 1)
	print s.threeSumClosest([-1,23,4,12,32,12], 17)
	print s.threeSumClosest([13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6], -59)
