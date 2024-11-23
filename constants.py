import sys
import os

class ScreenDimensionsError(Exception):

	def __init__(self, type: str) -> None:
		
		# type = 0 if both screen dimensions are values, 1 if both are 'auto', 2 if either are strings but not 'auto'

		messages = ['Both Screen Dimensions cannot be integers', 'Both Screen Dimensions cannot be set to auto', 'Invalid Screen Dimensions input']
		self.message = f'{messages[type]} in config.txt'
		super().__init__(self.message)

def save_path(relative_path: str) -> str:

    if getattr(sys, 'frozen', False): return os.path.join(os.getenv('APPDATA'), '08BitPixels/Tic Tac Toe AI/', relative_path)
    else: return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

def save(
		  	settings: dict[
				  
				'SCREEN_WIDTH': int | str, # value / 'auto'
				'SCREEN_HEIGHT': int | str, # value / 'auto'

				'COLS': int,
				'ROWS': int,
				'WIN_ROW': int,
				'GAMEMODE': int, # 0 / 1
				'FIRST_PLAYER': int, # 0 / 1

				'AI_LEVEL': int, # 0 / 1
				'AI_ACCURACY': int,
				'AI_PLAYER': int, # 0 / 1

				'BG_COLOUR': tuple[int, int, int] | str,
				'LINE_COLOUR': tuple[int, int, int] | str,
				'CIRC_COLOUR': tuple[int, int, int] | str,
				'CROSS_COLOUR': tuple[int, int, int] | str,

			]
			
		) -> None:

		print('\nSaving...')
		with open(save_path('config\\config.txt'), 'w') as config: 
			
			config.write(

f'''# CONFIG

## Screen Setup ----
{'\n'.join([f'{setting} = {data}' for setting, data in list(settings.items())[:2]])}

## Game Setup ----
{'\n'.join([f'{setting} = {data}' for setting, data in list(settings.items())[2:7]])}

## AI Setup ----
{'\n'.join([f'{setting} = {data}' for setting, data in list(settings.items())[7:10]])}

## Colours ----
{'\n'.join([f'{setting} = {data}' for setting, data in list(settings.items())[10:]])}

-----------------------------------------------------------------------------------------------------------------------------------
# CONFIG EXPLAINED

## Screen Setup ----
SCREEN WIDTH / HEIGHT: int = it will be that value, auto = will determine value from other value specified and the board dimensions
(AT LEAST ONE NEEDS TO BE AUTO, AND THEY CANNOT BOTH BE AUTO)

## Game Setup ----
COLS, ROWS: The dimensions of the board
WIN_ROW: How many someone is required to 'get in a row'
GAMEMODE: 0 = PvAI, 1 = PvP
FIRST_PLAYER: Which player goes first. P1 = Cross, P2 = Circle

## AI Setup ----
AI_LEVEL: 1 = AI uses Minimax algorithm, 0 = AI chooses a random move
AI_ACCURACY: -1 = Perfect (takes longest to think), 1 = Worst, Ranging from 1 upwards = Progressively Better

## Colours ----
BG_COLOUR: The colour of the board background
LINE_COLOUR: The colour of the lines on the board
CIRC_COLOUR: The colour of the circle icon
CROSS_COLOUR: The colour of the cross icon
(ALL COLOURS MUST BE THEIR HEXADECIMAL VALUES)'''

			)

		print('Saved')

def load_save() -> dict:

	if os.path.isfile(save_path('config\\config.txt')):

		with open(save_path('config\\config.txt'), 'r') as config_file: 

			config = {}
			contents = config_file.readlines()

			for line in contents[3:5] + contents[7:12] + contents[14:17] + contents[19:23]:

				setting = line.split(' = ')[0].strip('\n')
				data = line.split(' = ')[1].strip('\n')
				config[setting] = int(data) if data.strip('-').isnumeric() else data.lower()
		
			return config

	else:

		print('\nNo save file present; creating new one...')
		if not os.path.isdir(save_path('config\\')): os.makedirs(save_path('config\\'))
		save(settings = DEFAULT_CONFIG)
		return DEFAULT_CONFIG

def screen_dimensions(screen_dims: tuple[int | str, int | str], board_dims: tuple[int, int]) -> tuple[int, int]:

	cols, rows = board_dims
	width, height = screen_dims

	if width == 'auto' and height == 'auto': raise ScreenDimensionsError(type = 1)
	if isinstance(width, int) and isinstance(height, int): raise ScreenDimensionsError(type = 0)
	if (isinstance(width, str) and width != 'auto') or (isinstance(height, str) and height != 'auto'): raise ScreenDimensionsError(type = 2)

	if width == 'auto': width = int(cols * (height / rows))
	if height == 'auto': height = int(rows * (width / cols))

	return (width, height)

# Default Settings
DEFAULT_CONFIG = {

	'SCREEN_WIDTH': 'auto',
	'SCREEN_HEIGHT': 600,

	'COLS': 3,
	'ROWS': 3,
	'WIN_ROW': 3,
	'GAMEMODE': 0,
	'FIRST_PLAYER': 1, 

	'AI_LEVEL': 1,
	'AI_ACCURACY': -1,
	'AI_PLAYER': 2,

	'BG_COLOUR': '#1caa9c',
	'LINE_COLOUR': '#179187',
	'CIRC_COLOUR': '#efe7c8',
	'CROSS_COLOUR': '#424242'
	
}

config = load_save()

# Game Setup
COLS, ROWS = config['COLS'], config['ROWS']
WIN_ROW = config['WIN_ROW']
GAMEMODE = config['GAMEMODE'] # 0: PvAI, 1: PvP
FIRST_PLAYER = config['FIRST_PLAYER'] # P1 = cross | P2 = circle

# Screen Dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = config['SCREEN_WIDTH'], config['SCREEN_HEIGHT']
WIDTH, HEIGHT = screen_dimensions(screen_dims = (SCREEN_WIDTH, SCREEN_HEIGHT), board_dims = (COLS, ROWS))

# AI Setup
AI_LEVEL = config['AI_LEVEL'] # 1 = Minimax, 0 = Random
AI_ACCURACY = config['AI_ACCURACY'] # -1 = Perfect, 1 = Worst, >1 = Better
AI_PLAYER = config['AI_PLAYER'] # P1 / P2

# Colours
BG_COLOUR = config['BG_COLOUR']
LINE_COLOUR = config['LINE_COLOUR']
CIRC_COLOUR = config['CIRC_COLOUR']
CROSS_COLOUR = config['CROSS_COLOUR']

# Offset Dimensions
SQ_SIZE = WIDTH / COLS

LINE_WIDTH = int(SQ_SIZE / 12)
CIRC_WIDTH = LINE_WIDTH
CROSS_WIDTH = int(LINE_WIDTH * 1.25)
RADIUS = SQ_SIZE / 4

OFFSET = SQ_SIZE / 4
WIN_LINE_OFFSET = SQ_SIZE / 6