class Solution:
	def isValidNine(self, nine):
		drawer = [0]*9
		for e in nine:
			if e == ".":
				continue
			if drawer[int(e)-1] == 1:
				return False
			drawer[int(e)-1] = 1
		return True
	def isValidSudoku(self, board):
		# Check Each Row
		for i in range(0,9):
			if not self.isValidNine(board[i]):
				return False
		# Check Each Column
		for i in range(0,9):
			if not self.isValidNine([r[i] for r in board]):
				return False
		# Check Each Sub box
		for i in range(0,9,3):
			for j in range(0,9,3):
				if not self.isValidNine(board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3]):
					return False
		return True

if __name__ == "__main__":
	s = Solution()
	print s.isValidSudoku([[5,3,".",".",7,".",".",".","."], \
					      [6,".",".",1,9,5,".",".","."], \
					      [".",9,8,".",".",".",".",6,"."], \
					      [8,".",".",".",6,".",".",".",3], \
					      [4,".",".",8,".",3,".",".",1], \
					      [7,".",".",".",2,".",".",".",6], \
					      [".",6,".",".",".",".",2,8,"."], \
					      [".",".",".",4,1,9,".",".",5], \
					      [".",".",".",".",8,".",".",7,9]])
