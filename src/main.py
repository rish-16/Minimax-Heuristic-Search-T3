import copy, math, random
from sys import maxsize

board = [
	[".", ".", "."],
	[".", ".", "."],
	[".", ".", "."]
]

ai = "X"
human = "O"

def display(pos):
	for i in range(len(pos)):
		header = ""
		for j in range(len(pos[i])):
			header += " {} ".format(pos[i][j])
		print (header)
	print ()

def is_full(pos):
	for i in range(len(pos)):
		for j in range(len(pos[i])):
			if pos[i][j] == ".":
				return False
	return True
		
def get_states(pos, symbol):
	children = []

	for i in range(len(pos)):
		for j in range(len(pos[i])):
			if pos[i][j] == ".":
				board_copy = copy.deepcopy(pos)
				board_copy[i][j] = symbol
				children.append(board_copy)
				
	return children
	
def check_board(pos):
	n = 3
	# rows
	for r in range(n):
		yield [(r, c) for c in range(n)]

	# columns
	for c in range(n):
		yield [(r, c) for r in range(n)]

	# l2r
	yield [(i, i) for i in range(n)]
	
	# r2l
	yield [(i, n - 1 - i) for i in range(n)]
         
def is_winner(pos, symbol):
	for indexes in check_board(pos):
		if all(pos[r][c] == symbol for r, c in indexes):
			return True
	return False
	
def static_eval(pos):
	if is_full(pos):
		return 0
		
	
		
def get_possible_moves(pos):
	possible = []
	for i in range(len(pos)):
		for j in range(len(pos[i])):
			if pos[i][j] == ".":
				possible.append([i, j])
				
	return possible
		
def minimax(pos, depth, is_max):
	valid_locations = get_possible_moves(pos)
	is_terminal = is_full(pos)
	
	if depth == 0 or is_terminal:
		if is_terminal:
			pass
		else:
			return static_eval(pos)

	if is_max: # maximising player
		value = -math.inf
		row, col = random.choice(get_possible_moves(pos))
		
		for i in range(len(pos)):
			for j in range(len(pos[i])):
				if pos[i][j] == ".":
					b_copy = copy.deepcopy(pos)
					b_copy[i][j] = ai
					new_score = minimax(b_copy, depth - 1, False)[2]
					
					if new_score > value:
						value = new_score
						col = j
						row = i
		
		return [col, row, value]
		
	else: # minimising player
		value = math.inf
		row, col = random.choice(get_possible_moves(pos))
		
		for i in range(len(pos)):
			for j in range(len(pos[i])):
				if pos[i][j] == ".":
					b_copy = copy.deepcopy(pos)
					b_copy[i][j] = human
					new_score = minimax(b_copy, depth - 1, True)[2]
					
					if new_score < value:
						value = new_score
						col = j
						row = i
	
		return [col, row, value]
		
def make_move(pos, y, x, symbol):
	if pos[y][x] == ".":
		pos[y][x] = symbol
		
while not is_full(board) or not is_winner(board, ai) or not is_winner(board, human):
	human_y = int(input("Enter y: ")) - 1 # convert to board indices
	human_x = int(input("Enter x: ")) - 1 # convert to board indices
	
	make_move(board, human_y, human_x, human) # human
	ai_x, ai_y, score = minimax(board, 2, True) # ai
	make_move(board, ai_y, ai_x, ai)
	display(board)