from game import Game, Minimax

G = Game()
minimax = Minimax(G)

G.display()
x_turn = True

while G.is_full() == False:
	player_move_y = int(input("Enter y: "))
	player_move_x = int(input("Enter x: "))
	
	new_pos = G.make_move(player_move_y, player_move_x, x_turn)
	G.display(new_pos)
	minimax = minimax.solve(new_pos)
	
	best_move = 
	
	x_turn = False
	