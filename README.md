# Tic Tac Toe AI

A PvAI Tic Tac Toe game that uses the unbeatable Minimax Algorithm to play against you. <br>
_Built on Python using the PyGame module._

## How to Install Correctly
Go to the _Releases_ Page and download the .exe file in the latest release. <br>
_(Don't download the source code)_

## How to Play
- Click on a board square to make your move
- Press `[G]` to toggle gamemodes `(PvAI / PvP)`
- Press `[M]` to toggle the AI Level `(Intelligent / Random)`
- Press `[R]` to restart the game / start a new game

Most importantly - have fun!

## Configuration
_* All of this info is also in the text file (`config.txt`)_

Using config.txt (located at `%appdata%/08BitPixels/Tic Tac Toe AI/config`), you can configure;

### Screen Settings
- The dimensions of the screen `(width / height)`
    - If you enter a number: it will be that value
    - If you enter 'auto': will determine value from the other value specified and the board dimensions <br>
      _* At least one needs to be auto, and they cannot both be auto_

### Game Settings
- The size of the board `(cols + rows)`
- The starting gamemode `(0 = PvAI, 1 = PvP)`
- The first player to make a move `(P1 = Cross, P2 = Circle)`
- How many tiles are needed in a row to win
  
### AI Settings
- The level of the AI `(0 = Random, 1 = Intelligent - Minimax Algorithm)`
- The Accuracy of the AI `(-1 = Perfect, 1 = Worst, Ranging from 1 upwards = Progressively Better)`
- Which player the AI is `(1 = P1, 2 = P2)`
  
### Colours
- The colour of the board background
- The colour of the lines on the board
- The colour of the circle icon
- The colour of the cross icon

_* All colours must be in Hexadecimal_

## Credits
Thanks to ClearCode (https://www.youtube.com/@ClearCode) for teaching me how to use Pygame and to code this AI. He does loads of awesome Python and Pygame tutorials so if you want to learn how to use Pygame, I highly reccomend checking him out.
