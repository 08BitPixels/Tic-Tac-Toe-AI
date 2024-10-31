# Board Dimensions
COLS, ROWS = 3, 3
WIN_ROW = 3

# Game Setup
GAMEMODE = 0 # 0: PvAI, 1: PvP
FIRST_PLAYER = 1 # P1 = cross | P2 = circle

# AI Setup
AI_LEVEL = 1 # 1 = Minimax, 0 = Random
AI_ACCURACY = -1 # -1 = Perfect, 1 = Worst, >1 = Better
AI_PLAYER = 2 # P1 / P2

# Screen Dimensions
HEIGHT = 600
WIDTH = int(COLS * (HEIGHT / ROWS))

# Offset Dimensions
SQ_SIZE = WIDTH / COLS

LINE_WIDTH = int(SQ_SIZE / 12)
CIRC_WIDTH = LINE_WIDTH
CROSS_WIDTH = int(LINE_WIDTH * 1.25)
RADIUS = SQ_SIZE / 4

OFFSET = SQ_SIZE / 4
WIN_LINE_OFFSET = SQ_SIZE / 6

# Colours
BG_COLOUR = (28, 170, 156)
LINE_COLOUR = (23, 145, 135)
CIRC_COLOUR = (239, 231, 200)
CROSS_COLOUR = (66, 66, 66)

# Default Settings
DEFAULT_CONFIG = {
					
	'COLS': 3,
	'ROWS': 3,
	'WIN_ROW': 3,
	'GAMEMODE': 0,
	'FIRST_PLAYER': 1,
	'AI_LEVEL': 1,
	'AI_ACCURACY': -1,
	'AI_PLAYER': 2,
	'SCREEN_HEIGHT': 600,
	'SCREEN_WIDTH': 'auto'

}

TUTORIAL_TEXT = '''
CONFIG EXPLAINED ------------------------------

Game Setup ----
COLS, ROWS: The dimensions of the board
WIN_ROW: How many someone is required to 'get in a row'
GAMEMODE: 0 = PvAI, 1 = PvP
FIRST_PLAYER: Which player goes first. P1 = Cross, P2 = Circle

AI Setup ----
AI_LEVEL: 1 = AI uses Minimax algorithm, 0 = AI chooses a random move
AI_ACCURACY: -1 = Perfect (takes longest to think), 1 = Worst, Ranging from 1 upwards = Progressively Better

Screen Setup ----
SCREEN WIDTH / HEIGHT: int = it will be that value, auto = will determine value from other value specified and the board dimensions
'''