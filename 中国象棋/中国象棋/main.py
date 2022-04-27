import pgzrun
from pgzhelper import *
from chesses import *


WIDTH = 521
HEIGHT = 577

chessBoard = Actor("棋盘")



def draw():
	screen.clear()
	chessBoard.draw()
	mark1.draw()
	mark2.draw()
	DrawAllChesses()

def update():
	pass

	

def on_mouse_up(pos):
	checkMoveAndEat(pos)
	printChessInfo()

pgzrun.go()