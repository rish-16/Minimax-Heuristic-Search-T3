import copy, math, random
from sys import maxsize

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
	 
def get_static_evaluation(pos):
	if is_winner(pos, ai) == True:
		return [-1, -1, 1]
	elif is_winner(pos, human) == True:
		return [-1, -1, -1]
	elif is_full(pos) == True:
		return [-1, -1, 0]
	else:
		return [-1, -1, 0]
	
		
def minimax(pos, depth, is_max):
	static_eval = get_static_evaluation(pos)
	
	# return static evaluation only at terminal states
	if depth == 0 or is_terminal(pos) == True:
		return static_eval

	if is_max: # maximising player
		value = -math.inf
		row, col = random.choice(get_possible_moves(pos))
		
		# searching all children of current position
		for i in range(len(pos)):
			for j in range(len(pos[i])):
				if pos[i][j] == ".":
					b_copy = copy.deepcopy(pos)
					b_copy[i][j] = ai
					new_score = minimax(b_copy, depth - 1, False)[2]
					
					# choosing best move
					if new_score < value:
						value = new_score
						row = i
						col = j
		
		return [row, col, value]
		
	else: # minimising player
		value = math.inf
		row, col = random.choice(get_possible_moves(pos))
		
		for i in range(len(pos)):
			for j in range(len(pos[i])):
				if pos[i][j] == ".":
					b_copy = copy.deepcopy(pos)
					b_copy[i][j] = human
					new_score = minimax(b_copy, depth - 1, True)[2]
					
					if new_score > value:
						value = new_score
						row = i
						col = j
	
		return [row, col, value]
		
def make_move(pos, y, x, symbol):
	if pos[y][x] == ".":
		pos[y][x] = symbol
		
num_draws = 0
ai_1_wins = 0
ai_2_wins = 0

for i in range(100):
	board = [
		[".", ".", "."],
		[".", ".", "."],
		[".", ".", "."]
	]
	while is_terminal(board) == False:

		# human_y = int(input("Enter y: ")) - 1 # convert to board indices
		# human_x = int(input("Enter x: ")) - 1 # convert to board indices
		ai1_y, ai1_x, human_score = minimax(board, 3, False)
		make_move(board, ai1_y, ai1_x, human) # ai1
		# display(board)
		
		ai_win = is_winner(board, ai)
		human_win = is_winner(board, human)
		
		if ai_win != human_win:
			if ai_win == True:
				print ("AI Win")
				ai_1_wins += 1
				break
			elif human_win == True:
				print ("Human Win")
				ai_2_wins +=1 
				break
		elif is_full(board) == True:
			num_draws += 1
			break
		else:
			pass
			
		ai_y, ai_x, score = minimax(board, 3, True) # ai2
		make_move(board, ai_y, ai_x, ai)
		# display(board)
		
		ai_win = is_winner(board, ai)
		human_win = is_winner(board, human)
		
		if ai_win != human_win:
			if ai_win == True:
				print ("AI Win")
				ai_1_wins += 1
				break
			elif human_win == True:
				print ("Human Win")
				ai_2_wins +=1 
				break
		elif is_full(board) == True:
			num_draws += 1
			break
		else:
			pass
			
print (num_draws, ai_1_wins, ai_2_wins)