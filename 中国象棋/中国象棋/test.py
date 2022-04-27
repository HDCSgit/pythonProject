class Chess():
	def __init__(self,type):
		self.chessType = type

class ChessConst():
	RED_CHE = 1
	RED_HORSE = 2
	
	
		
ma = Chess(ChessConst.RED_CHE)

list2D = [
	[ma,2,3],
	[4,5,6]
]

print(list2D[0][0].chessType)