class Solution:
	# @param board, a 2D array
	# Capture all regions by modifying the input board in-place.
	# Do not return any value.
	def solve(self, board):
		if len(board) == 0:
			return
		h = len(board)
		w = len(board[0])
		for i in range(h):
			if board[i][0] == "O": self.search(board, i, 0)
			if board[i][w-1] == "O": self.search(board, i, w-1)
		for j in range(w):
			if board[0][j] == "O": self.search(board, 0, j)
			if board[h-1][j] == "O": self.search(board, h-1, j)
		for i in range(h):
			for j in range(w):
				if board[i][j] == "L": board[i][j] = "O"
				elif board[i][j] == "O": board[i][j] = "X"
	# BFS
	def search(self, board, x, y):
		stack = [(x,y)]
		h = len(board)
		w = len(board[0])
		while len(stack) > 0:
			x,y = stack.pop(0)
			if x < 0 or y < 0 or x >= h or y >= w:
				continue
			if board[x][y] == "X" or board[x][y] == "L":
				continue
			board[x][y] = "L"	
			stack.append((x-1,y))
			stack.append((x+1,y))
			stack.append((x,y-1))
			stack.append((x,y+1))

if __name__ == "__main__":
	board = [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
	s = Solution()
	s.solve(board)
	print board
