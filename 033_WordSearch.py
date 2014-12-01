class Solution:
	# direction: 0 up, 1 down, 2 left, 3 right
	def search(self, board, word, visited, direction, x, y, index):
		if index  == len(word):
			return True
		row = len(board)
		column = len(board[0])
		if direction != 0 and x + 1 < row:
			if visited[(x+1)*column+y] == 0 and board[x+1][y] == word[index]:
				visited[(x+1)*column+y] = 1
				if self.search(board, word, visited, 1, x+1, y, index+1):
					return True
				visited[(x+1)*column+y] = 0
		if direction != 1 and x > 0:
			if visited[(x-1)*column+y] == 0 and board[x-1][y] == word[index]:
				visited[(x-1)*column+y] = 1
				if self.search(board, word, visited, 0, x-1, y, index+1):
					return True
				visited[(x-1)*column+y] = 0
		if direction != 2 and y + 1 < column:
			if visited[x*column+y+1] == 0 and board[x][y+1] == word[index]:
				visited[x*column+y+1] = 1
				if self.search(board, word, visited, 3, x, y+1, index+1):
					return True
				visited[x*column+y+1] = 0
		if direction != 3 and y > 0:
			if visited[x*column+y-1] == 0 and board[x][y-1] == word[index]:
				visited[x*column+y-1] = 1
				if self.search(board, word, visited, 2, x, y-1, index+1):
					return True
				visited[x*column+y-1] = 0
		return False
	def exist(self, board, word):
		row = len(board)
		column = len(board[0])
		visited = [0] * (row * column)
		for i in range(row):
			for j in range(column):
				if board[i][j] == word[0]:
					visited[i*column+j] = 1
					if self.search(board, word, visited, -1, i, j, 1):
						return True
					visited[i*column+j] = 0
		return False

if __name__ == "__main__":
	s = Solution()
	board = [ "ABCE", "SFCS", "ADEE" ]
	board = ["FYCENRD","KLNFINU","AAARAHR","NDKLPNE","ALANSAP","OOGOTPN","HPOLANO"]
	board = ["ABCE","SFES","ADEE"]
	print s.exist(board, "ABCESEEEFS")
