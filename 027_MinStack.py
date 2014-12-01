class MinStack:
	def __init__(self):
		self.stack = []
		self.minStack = []
		self.minCounter = []
	# @param x, an integer
	# @return an integer
	def push(self, x):
		self.stack.append(x)
		if len(self.minStack) == 0 or x < self.minStack[-1]:
			self.minStack.append(x)
			self.minCounter.append(1)
		elif x == self.minStack[-1]:
			self.minCounter[-1] += 1
	# @return nothing
	def pop(self):
		if len(self.stack) == 0:
			return
		if self.stack.pop() == self.minStack[-1]:
			if self.minCounter[-1] == 1:
				self.minStack.pop()
				self.minCounter.pop()
			else:
				self.minCounter[-1] -= 1
	# @return an integer
	def top(self):
		if len(self.stack) > 0:
			return self.stack[-1]
		else:
			return 0
	# @return an integer
	def getMin(self):
		return self.minStack[-1]

if __name__ == "__main__":
	s = MinStack()
	s.push(2147483646)
	s.push(2147483646)
	s.push(2147483647)
	s.top()
	s.pop()
	print s.getMin()
	s.pop()
	print s.getMin()
	s.pop()
	s.push(2147483647)
	s.top()
	print s.getMin()
	s.push(-2147483648)
	s.top()
	print s.getMin()
	s.pop()
	print s.getMin()
