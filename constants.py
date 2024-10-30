# Board Dimensions
COLS, ROWS = 4, 4
WIN_ROW = 3

# Game Setup
GAMEMODE = 'PvAI' # PvAI  or PvP
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