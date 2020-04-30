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

def get_possible_moves(pos):
	possible = []
	for i in range(len(pos)):
		for j in range(len(pos[i])):
			if pos[i][j] == ".":
				possible.append([i, j])
				
	return possible
	
def is_terminal(pos):
	return is_full(pos) or is_winner(pos, ai) or is_winner(pos, human)
		
def minimax(pos, depth, is_max):
	term = is_terminal(pos)
	
	if depth == 0 or term == True:
		if term == True:
			if is_winner(pos, ai):
				return [-1, -1, 100000000000]
			elif is_winner(pos, human):
				return [-1, -1, -100000000000]
			elif is_full(pos):
				return [-1, -1, 0]
		else: # depth is 0
			return [-1, -1, 0]

	if is_max == True: # maximising player
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
		
while is_terminal(board) == False:

	human_y = int(input("Enter y: ")) - 1 # convert to board indices
	human_x = int(input("Enter x: ")) - 1 # convert to board indices
	make_move(board, human_y, human_x, human) # human
	display(board)
	
	ai_win = is_winner(board, ai)
	human_win = is_winner(board, human)
	
	if ai_win == human_win == True:
		print ("Draw")
		break
	elif ai_win != human_win:
		if ai_win == True:
			print ("AI Win")
			break
		elif human_win == True:
			print ("Human Win")
			break
	else:
		pass
		
	ai_x, ai_y, score = minimax(board, 2, True) # ai
	make_move(board, ai_y, ai_x, ai)
	display(board)
	
	ai_win = is_winner(board, ai)
	human_win = is_winner(board, human)
	
	if ai_win == human_win == True:
		print ("Draw")
		break
	elif ai_win != human_win:
		if ai_win == True:
			print ("AI Win")
			break
		elif human_win == True:
			print ("Human Win")
			break
	else:
		pass