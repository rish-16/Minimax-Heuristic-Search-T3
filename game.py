class Game:
	def __init__(self, pos=None):
		if pos == None:
			self.board = [["_" for j in range(3)] for i in range(3)]
		else:
			self.board = pos
		self.x_turn = True # X starts

	def copy_board(self, pos):
		copy = []
		for i in range(len(pos)):
			temp = []
			for j in range(len(pos[i])):
				temp.append(pos[i][j])
			copy.append(temp)

		return copy

	def display(self, pos):
		for i in range(len(board)):
			header = ""
			footer = ""
			for j in range(len(board[i])):
				header += "| {} |".format(board[i][j])
				footer += "-----"
			print (header)
			print (footer)

	def make_move(self, y, x, x_turn):
		symbol = "X" if x_turn else "O"
		
		self.board[y][x] = symbol
		if self.x_turn == False:
			self.x_turn = True
		elif self.x_turn == True:
			self.x_turn = False
			
		return self.board

	def get_board_states(self, pos, x_turn):
		symbol = "X" if x_turn == True else "O"
		children = []
		for i in range(3):
			for j in range(3):
				if pos[i][j] == " ":
					child_board = self.copy_board(pos)
					child_board[i][j] = symbol
					children.append(child_board)
					
		return children

	def win_indexes(self, n):
		# rows
		for r in range(n):
			yield [[r, c] for c in range(n)]

		# columns
		for c in range(n):
			yield [[r, c] for r in range(n)]

		# l2r
		yield [[i, i] for i in range(n)]

		# r2l
		yield [[i, n - 1 - i] for i in range(n)]

	def is_winner(self, pos, symbol):
		n = len(pos)
		for indexes in self.win_indexes(n):
			if all(pos[r][c] == symbol for r, c in indexes):
				return True
		return False

	def get_static_eval(self, pos):
		X_wins = self.is_winner(pos, "X")
		O_wins = self.is_winner(pos, "O")
		
		if X_wins == O_wins:
			return 0 # draw
		elif O_wins == True and X_wins == False:
			return -1 # O wins
		elif X_wins == True and O_wins == False:
			return 1 # X wins
			
	def is_full(self, pos):
		for i in range(len(pos)):
			for j in range(len(pos[i])):
				if pos[i][j] == " ":
					return False
					
		return True
		
class Minimax:
	def __init__(self, engine):
		self.engine = engine
	
	def solve(self, pos):
		static_eval = self.engine.get_static_eval(pos)
		if static_eval != 0:
			return static_eval
			
		if self.engine.is_full(pos):
			return 0
			
		# Rollout of game states
		x_turn = self.engine.turn
		branches = self.engine.get_board_states(pos, x_turn)
		branch_evals = [self.solve(branch) for branch in branches]
		print (branch_evals)
		
		if x_turn == True:
			if 1 in branch_evals:
				return "X Wins"
			elif 0 in branch_evals:
				return "Draw"
			else:
				return "O Wins"
				
		else:
			if -1 in branch_evals:
				return "O Wins"
			elif 0 in branch_evals:
				return "Draw"
			else:
				return "X Wins"