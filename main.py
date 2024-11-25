import pygame
import sys
import os

from copy import deepcopy
from time import time
from random import choice
from numpy import zeros

from constants import *

def resource_path(relative_path: str) -> str: 

    try: base_path = sys._MEIPASS
    except Exception: base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe AI')
pygame.display.set_icon(pygame.image.load(resource_path('images/icon.ico')).convert_alpha())

class Game:

	def __init__(self) -> None:
		
		self.board = Board()
		self.ai = AI(game = self, level = AI_LEVEL, player = AI_PLAYER, accuracy = AI_ACCURACY)
		self.gamemode = GAMEMODE
		self.running = True
		self.player = FIRST_PLAYER
		self.show_lines()

	def make_move(self, col: int, row: int) -> None:

		self.board.mark_sq(col, row, self.player)
		self.draw_fig(col, row)
		self.next_turn()

		pygame.display.update() # Update the screen

		if self.is_over(): 

			self.running = False

			if self.board.final_state(show = False) == 0: print('\nGAME OVER: Draw')
			else: print(f'\nGAME OVER: Player {int(self.board.final_state(show = False))} Wins')

			print('Press [R] to start a new game')

	def show_lines(self) -> None:

		screen.fill(BG_COLOUR)
		# Draws lines for the board
		for line in range(COLS - 1): # vertical
			pygame.draw.line(screen, LINE_COLOUR, (SQ_SIZE * (line + 1), 0), (SQ_SIZE * (line + 1), HEIGHT), LINE_WIDTH)

		for line in range(ROWS - 1): # horizontal
			pygame.draw.line(screen, LINE_COLOUR, (0, SQ_SIZE * (line + 1)), (WIDTH, SQ_SIZE * (line + 1)), LINE_WIDTH)

		pygame.display.update() # Update the screen

	def draw_fig(self, col: int, row: int) -> None:

		if self.player == 1: # Draw a cross

			start_desc = (col * SQ_SIZE + OFFSET, row * SQ_SIZE + OFFSET)
			end_desc = (col * SQ_SIZE + SQ_SIZE - OFFSET, row * SQ_SIZE + SQ_SIZE - OFFSET)
			pygame.draw.line(screen, CROSS_COLOUR, start_desc, end_desc, CROSS_WIDTH)

			start_asc = (col * SQ_SIZE + SQ_SIZE - OFFSET, row * SQ_SIZE + OFFSET)
			end_asc = (col * SQ_SIZE + OFFSET, row * SQ_SIZE + SQ_SIZE - OFFSET)
			pygame.draw.line(screen, CROSS_COLOUR, start_asc, end_asc, CROSS_WIDTH)

		elif self.player == 2: # Draw a circle

			center = (col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2)
			pygame.draw.circle(screen, CIRC_COLOUR, center, RADIUS, CIRC_WIDTH)

		pygame.display.update() # Update the screen

	def next_turn(self) -> None:
		self.player = (self.player % 2) + 1

	def change_gamemode(self) -> None:
		self.gamemode = (self.gamemode + 1) % 2

	def reset(self) -> None:

		self.board = Board()
		self.running = True
		self.player = FIRST_PLAYER
		self.show_lines()

	def is_over(self) -> bool:
		return self.board.final_state(show = True) != 0 or self.board.is_full()

	def time_convert(self, secs: float, rd: int) -> str:

		mins = secs // 60
		seconds = secs % 60
		mins %= 60

		return f'{int(mins)} Minutes, {round(seconds, rd)} Seconds'

class Board:

	def __init__(self) -> None:

		self.squares = zeros((ROWS, COLS))
		self.empty_sqs = self.squares
		self.marked_sqs = 0

	def final_state(self, show: bool | None = False) -> int:

		# Return 0 if there is no win yet
		# Return 1 if Player 1 wins
		# Return 2 if Player 2 wins

		# Vertical Wins

		for col in range(COLS):

			for line in range(ROWS - (WIN_ROW - 1)):

				squares = [self.squares[line + i][col] for i in range(WIN_ROW)]

				if all(sq == 1 for sq in squares) or all(sq == 2 for sq in squares):

					if show:

						colour = CIRC_COLOUR if self.squares[line][col] == 2 else CROSS_COLOUR
						i_pos = ((col * SQ_SIZE) + (SQ_SIZE // 2), (line * SQ_SIZE) + WIN_LINE_OFFSET)
						f_pos = ((col * SQ_SIZE) + (SQ_SIZE // 2), ((line + WIN_ROW) * SQ_SIZE) - WIN_LINE_OFFSET)
						pygame.draw.line(screen, colour, i_pos, f_pos, LINE_WIDTH)

						pygame.display.update() # Update the screen

					return self.squares[line][col]

		# Horizontal wins
		for row in range(ROWS):

			for line in range(COLS - (WIN_ROW - 1)):

				squares = [self.squares[row][line + i] for i in range(WIN_ROW)]

				if all(sq == 1 for sq in squares) or all(sq == 2 for sq in squares):

					if show:

						colour = CIRC_COLOUR if self.squares[row][line] == 2 else CROSS_COLOUR
						i_pos = ((line * SQ_SIZE) + WIN_LINE_OFFSET, (row * SQ_SIZE) + (SQ_SIZE // 2))
						f_pos = (((line + WIN_ROW) * SQ_SIZE) - WIN_LINE_OFFSET, (row * SQ_SIZE) + (SQ_SIZE // 2))
						pygame.draw.line(screen, colour, i_pos, f_pos, LINE_WIDTH)

						pygame.display.update() # Update the screen

					return self.squares[row][line]

		# Diagonal wins
		for row in range(ROWS - (WIN_ROW - 1)): # Descending

			for col in range(COLS - (WIN_ROW - 1)):

				squares = [self.squares[row + i][col + i] for i in range(WIN_ROW)]

				if all(sq == 1 for sq in squares) or all(sq == 2 for sq in squares):

					if show:

						colour = CIRC_COLOUR if self.squares[row + 1][col + 1] == 2 else CROSS_COLOUR
						i_pos = ((col * SQ_SIZE) + WIN_LINE_OFFSET, (row * SQ_SIZE) + WIN_LINE_OFFSET)
						f_pos = (((col + WIN_ROW) * SQ_SIZE) - WIN_LINE_OFFSET, ((row + WIN_ROW) * SQ_SIZE) - WIN_LINE_OFFSET)
						pygame.draw.line(screen, colour, i_pos, f_pos, CROSS_WIDTH)

						pygame.display.update() # Update the screen

					return self.squares[row + 1][col + 1]

		for row in range(ROWS - (WIN_ROW - 1)): # Ascending

			for col in range(COLS - (WIN_ROW - 1)):

				squares = [self.squares[row + i][(col + (WIN_ROW - 1)) - i] for i in range(WIN_ROW)]

				if all(sq == 1 for sq in squares) or all(sq == 2 for sq in squares):

					if show:

						colour = CIRC_COLOUR if self.squares[row + 1][col + 1] == 2 else CROSS_COLOUR
						i_pos = ((col * SQ_SIZE) + WIN_LINE_OFFSET, ((row + WIN_ROW) * SQ_SIZE) - WIN_LINE_OFFSET)
						f_pos = (((col + WIN_ROW) * SQ_SIZE) - WIN_LINE_OFFSET, (row * SQ_SIZE) + WIN_LINE_OFFSET)
						pygame.draw.line(screen, colour, i_pos, f_pos, CROSS_WIDTH)

						pygame.display.update() # Update the screen

					return self.squares[row + 1][col + 1]

		return 0 # No win yet

	def mark_sq(self, col: int, row: int, player: int) -> None:

		self.squares[row][col] = player
		self.marked_sqs += 1

	def empty_sq(self, col: int, row: int) -> bool:
		return self.squares[row][col] == 0

	def get_empty_sqs(self) -> list:

		empty_sqs = []

		for col in range(COLS):

			for row in range(ROWS):

				if self.empty_sq(col, row):
					empty_sqs.append((col, row))

		return empty_sqs

	def is_full(self) -> bool:
		return self.marked_sqs == COLS * ROWS

	def is_empty(self) -> bool:
		return self.marked_sqs == 0

class AI:

	def __init__(self, game: Game, level: int, player: int, accuracy: int = -1) -> None:

		self.level = level
		self.player = player
		self.accuracy = accuracy
		self.game = game

	def rnd(self, board: Board) -> int:
		return choice(board.get_empty_sqs())

	def minimax(self, board: Board, maximising: bool, iter: int) -> tuple: # -> eval, move

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				pygame.quit()
				exit()

		if iter == self.accuracy: return 0, None
		else: iter += 1

		case = board.final_state() # Terminal Case

		if case != self.player and case != 0: return -1, None # AI loses
		if case == self.player: return 1, None # AI wins
		elif board.is_full(): return 0, None # Draw

		if maximising:

			max_eval = 100
			best_move = None
			empty_sqs = board.get_empty_sqs()

			for (col, row) in empty_sqs:

				temp_board = deepcopy(board)
				temp_board.mark_sq(col, row, 1 if self.player == 2 else 2)
				eval = self.minimax(temp_board, False, iter)[0]

				if eval < max_eval:

					max_eval = eval
					best_move = (col, row)

			return max_eval, best_move

		elif not maximising:

			min_eval = -100
			best_move = None
			empty_sqs = board.get_empty_sqs()

			for (col, row) in empty_sqs:

				temp_board = deepcopy(board)
				temp_board.mark_sq(col, row, self.player)
				eval = self.minimax(temp_board, True, iter)[0]

				if eval > min_eval:

					min_eval = eval
					best_move = (col, row)

			return min_eval, best_move

	def eval(self, main_board: Board) -> tuple: # -> move

		if self.level == 0: # Random choice

			start_time = time()
			eval = 'random'
			move = self.rnd(main_board)
			end_time = time()

		elif self.level == 1: # Minimax algorithm choice

			start_time = time()
			eval, move = self.minimax(main_board, False, 0)
			end_time = time()

		print(f"Player {self.player} (AI) moved in Position: {move}, Evalution: {eval}. ({self.game.time_convert(end_time - start_time, 2)})")

		return move # row, col

	def change_level(self) -> None:
		self.level = (self.level + 1) % 2

def main():

	game = Game()
	board = game.board
	ai = game.ai

	print(f'''
---------- TIC TAC TOE AI ----------
		  
Screen Dimensions: {WIDTH} x {HEIGHT}
Board Dimensions: {COLS} x {ROWS}
Win Row: {WIN_ROW}
Gamemode: {['PvAI', 'PvP'][game.gamemode]}

AI Level: {AI_LEVEL} ({['Random', 'Intelligent - Minimax Algorithm'][AI_LEVEL]})
AI Accuracy: {AI_ACCURACY} {'(Perfect)' if AI_ACCURACY == -1 else ''}

------------- New Game -------------
	''')

	while True:

		for event in pygame.event.get():

			# If you close the pygame window
			if event.type == pygame.QUIT:

				data = {

					'SCREEN_WIDTH': SCREEN_WIDTH,
					'SCREEN_HEIGHT': SCREEN_HEIGHT,

					'COLS': COLS,
					'ROWS': ROWS,
					'WIN_ROW': WIN_ROW,
					'GAMEMODE': GAMEMODE,
					'FIRST_PLAYER': FIRST_PLAYER, 

					'AI_LEVEL': AI_LEVEL,
					'AI_ACCURACY': AI_ACCURACY,
					'AI_PLAYER': AI_PLAYER,

					'BG_COLOUR': BG_COLOUR,
					'LINE_COLOUR': LINE_COLOUR,
					'CIRC_COLOUR': CIRC_COLOUR,
					'CROSS_COLOUR': CROSS_COLOUR
					
				}
				save(settings = data)
				pygame.quit()
				sys.exit()

			# Keypresses
			if event.type == pygame.KEYDOWN:

				# g = Switch Gamemode (Default: PvAI, Other: PvP)
				if event.key == pygame.K_g:

					game.change_gamemode()
					print(f'Gamemode: {['PvAI', 'PvP'][game.gamemode]}\n')

				# r = Restart the Game
				if event.key == pygame.K_r:

					game.reset()
					board = game.board
					ai = game.ai
					print('''\n------------- New Game -------------\n''')			

				# Toggle between Intelligent + Random
				if event.key == pygame.K_m: 
					
					ai.change_level()
					print(f'AI Level: {ai.level} ({['Random', 'Intelligent - Minimax Algorithm'][ai.level]})')

			# Mouse Clicks
			if event.type == pygame.MOUSEBUTTONDOWN:

				pos = event.pos
				col = int(pos[0] // SQ_SIZE)
				row = int(pos[1] // SQ_SIZE)

				if board.empty_sq(col, row) and game.running:

					print(f'Player {game.player} moved in Position: {(col, row)}')
					game.make_move(col, row)

		if game.gamemode == 0 and game.player == ai.player and game.running:

			col, row = ai.eval(board)
			game.make_move(col, row)

if __name__ == '__main__': main()