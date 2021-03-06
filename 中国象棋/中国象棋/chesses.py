import pgzrun
import math
from pgzhelper import *

#左上角(0,0)坐标的为(30,30)，格子间距离57
#Coordinate表示游戏坐标；Position表示棋子位置，左上角为(0,0)，右上角为(0,8)
#coX,coY				posX,posY

#棋子位置转换为游戏坐标
def Pos2Co(posX,posY):
	return 57.5 * posX + 30,57.5 * posY + 30

#游戏坐标转换为棋子位置
def Co2Pos(coX,coY):
	x = coX // 57.5
	x = x if x >= 0 else 0
	x = x if x <= 8 else 8
	x = math.floor(x)
	y = coY // 57.5
	y = y if y >= 0 else 0
	y = y if y <= 9 else 9
	y = math.floor(y)
	return x,y

class PlayerSideConst():
	RED = 0
	BLACK = 1

class ChessTypeConst():
	CHESS_NONE = 0

	RED_CHE = 1
	RED_HORSE = 2
	RED_XIANG = 3
	RED_SHI = 4
	RED_SHUAI = 5
	RED_PAO = 6
	RED_BING = 7

	BLACK_CHE = 11
	BLACK_HORSE = 12
	BLACK_XIANG = 13
	BLACK_SHI = 14
	BLACK_JIANG = 15
	BLACK_PAO = 16
	BLACK_ZU = 17

def getPlayerSide(chessType):
	if chessType == ChessTypeConst.CHESS_NONE:
		return 2
	return math.floor(chessType/10)

#空位置
class NoneChess():
	def __init__(self,posX,posY):
		self.chessType = ChessTypeConst.CHESS_NONE
		self.posX = posX
		self.posY = posY

	def draw(self):
		pass

	def checkCanMove(self,posX,posY):
		return False

noneChess = NoneChess(-1,-1)

ChessInfo = [
#PosX→	#0			#1		#2			#3		#4			#5		#6		#7			#8	  #PosY↓
	[noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess],#0
	[noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess],#1
	[noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess],#2
	[noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess],#3
	[noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess],#4
	[noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess],#5
	[noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess],#6
	[noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess],#7
	[noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess],#8
	[noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess,noneChess] #9
]


#棋子和Mark的父类
class Moveble(Actor):
	def __init__(self, image,posX = 0,posY = 0,pos=POS_TOPLEFT, anchor=ANCHOR_CENTER,**kwargs):
		super().__init__(image, pos, anchor, **kwargs)
		#棋子的位置坐标
		self.posX = posX
		self.posY = posY
		self.chessMove2PosXY(posX,posY)

	#根据棋子位置移到指定位置
	def chessMove2PosXY(self,posX,posY):
		#ChessInfo[self.posY][self.posX] = noneChess
		self.posX = posX
		self.posY = posY
		self.pos = 57.5 * posX + 30,57.5 * posY + 30
		#ChessInfo[posY][posX] = self

	#根据坐标移到指定位置
	def chessMove2CoXY(self,coX,coY):
		posX,posY = Co2Pos(coX,coY)
		self.chessMove2PosXY(posX,posY)

#跟着鼠标移动的四方形
class Mark(Moveble):
	def __init__(self, image,posX = 0,posY = 0,pos=POS_TOPLEFT, anchor=ANCHOR_CENTER,**kwargs):
		super().__init__(image , posX,posY,pos, anchor,**kwargs)

mark1 = Mark("四方形标志",posX = -1,posY = -1)
mark2 = Mark("四方形标志",posX = -1,posY = -1)

curSelectedChess = noneChess
curPlayerSide = PlayerSideConst.RED

def moveOrEat(posX,posY):
	global curSelectedChess
	global curPlayerSide
	curSelectedChess.chessMove2PosXY(posX,posY)
	mark2.chessMove2PosXY(posX,posY)
	curPlayerSide = (curPlayerSide + 1) % 2
	curSelectedChess = noneChess

def checkMoveAndEat(pos):
	coX,coY = pos[0],pos[1]
	posX,posY = Co2Pos(coX,coY)
	targetChess = ChessInfo[posY][posX]
	global curSelectedChess
	global curPlayerSide

	#选中棋子时
	if targetChess.chessType != ChessTypeConst.CHESS_NONE:
		#选中对方棋子
		if getPlayerSide(targetChess.chessType) != curPlayerSide:
			#可以移动；吃掉对方棋子
			if curSelectedChess.checkCanMove(posX,posY):
				moveOrEat(posX,posY)
		#选中当前玩家棋子
		else:
			mark1.chessMove2PosXY(posX,posY)
			mark2.chessMove2PosXY(posX,posY)
			curSelectedChess = targetChess
	#目标位置为空时
	else:
		#空位置可移动
		if curSelectedChess.checkCanMove(posX,posY):
			moveOrEat(posX,posY)
		#空位置不可移动
		else:
			return
		
	


#棋子父类
class Chess(Moveble):
	def __init__(self, image,posX = 0,posY = 0,pos=POS_TOPLEFT, anchor=ANCHOR_CENTER, chessType = ChessTypeConst.CHESS_NONE,**kwargs):
		super().__init__(image , posX,posY,pos, anchor,**kwargs)
		#棋子类型；默认为空类型
		self.chessType = chessType
		self.curCanMovePos = []

	#根据棋子位置移到指定位置
	def chessMove2PosXY(self,posX,posY):
		ChessInfo[self.posY][self.posX] = noneChess
		super().chessMove2PosXY(posX,posY)
		ChessInfo[posY][posX] = self

	#先定义通用的棋子能否移动判断
	def checkCanMove(self,posX,posY):
		targetChess = ChessInfo[posY][posX]
		if targetChess != noneChess:
			targetSide = getPlayerSide(targetChess.chessType)
			selfSide = getPlayerSide(self.chessType)
			#如果目标位置是自己颜色的棋子；不能移动
			if targetSide == selfSide:
				return False
		targetChess = ChessInfo[posY][posX]
		for i,v in enumerate(self.getCurCanMovePos()):
			if v.posX == posX and v.posY == posY:
				return True
		return False

	def getCurCanMovePos(self):
		self.resetCanMovePos()
		return self.curCanMovePos

	def resetCanMovePos(self):
		self.curCanMovePos = []

	def addToCurCanMovePos(self,posX,posY):
		tempChess = ChessInfo[posY][posX]
		targetSide = getPlayerSide(tempChess.chessType)
		if tempChess.chessType == ChessTypeConst.CHESS_NONE:
			self.curCanMovePos.append(NoneChess(posX,posY))
		elif targetSide != curPlayerSide:
			self.curCanMovePos.append(tempChess)




class Che(Chess):
	def resetCanMovePos(self):
		super().resetCanMovePos()
		tempPosX = self.posX - 1
		offSetX = -1	#向左遍历
		while(True):
			if tempPosX < 0:
				tempPosX = self.posX + 1 
				offSetX = 1		#碰到左边界，调头向右
				continue
			elif tempPosX > 8:	#碰到右边界，退出
				break
			tempChess = ChessInfo[self.posY][tempPosX]
			targetSide = getPlayerSide(tempChess.chessType)
			#判断为空棋子;空棋子加入可移动列表
			if tempChess.chessType == ChessTypeConst.CHESS_NONE:
				self.curCanMovePos.append(NoneChess(tempPosX,self.posY))
			else:
			#非空棋子则掉头；敌方则加入可移动列表
				if targetSide != curPlayerSide:
					self.curCanMovePos.append(tempChess)
				if offSetX == 1:#已经调过头；直接退出
					break
				tempPosX = self.posX
				offSetX = 1#调头
			tempPosX += offSetX
			

		tempPosY = self.posY - 1
		offSetY = -1
		while(True):
			if tempPosY < 0:
				tempPosY = self.posY + 1
				offSetY = 1
				continue
			elif tempPosY > 9:
				break
			tempChess = ChessInfo[tempPosY][self.posX]
			targetSide = getPlayerSide(tempChess.chessType)
			if tempChess.chessType == ChessTypeConst.CHESS_NONE:
				self.curCanMovePos.append(NoneChess(self.posX,tempPosY))
			else:
				if targetSide != curPlayerSide:
					self.curCanMovePos.append(tempChess)
				if offSetY == 1:
					break
				tempPosY = self.posY
				offSetY = 1
			tempPosY += offSetY


redChe1 = Che("红车",posX = 0,posY = 9,chessType = ChessTypeConst.RED_CHE)
redChe2 = Che("红车",posX = 8,posY = 9,chessType = ChessTypeConst.RED_CHE)
blackChe1 = Che("黑车",posX = 0,posY = 0,chessType = ChessTypeConst.BLACK_CHE)
blackChe2 = Che("黑车",posX = 8,posY = 0,chessType = ChessTypeConst.BLACK_CHE)

class Horse(Chess):
	def resetCanMovePos(self):
		super().resetCanMovePos()
		#向上走;没顶格，没被棋子挡住马脚
		if self.posY >= 2 and ChessInfo[self.posY - 1][self.posX].chessType == ChessTypeConst.CHESS_NONE:
			#左上;向上两格，向左一格
			if self.posX >= 1:
				self.addToCurCanMovePos(self.posX - 1,self.posY - 2)
			#右上;向上两格，向右一格
			if self.posX <= 7:
				self.addToCurCanMovePos(self.posX + 1,self.posY - 2)
		#向下走;
		if self.posY <= 7 and ChessInfo[self.posY + 1][self.posX].chessType == ChessTypeConst.CHESS_NONE:
			if self.posX >= 1:
				self.addToCurCanMovePos(self.posX - 1,self.posY + 2)
			if self.posX <= 7:
				self.addToCurCanMovePos(self.posX + 1,self.posY + 2)
		#向左走
		if self.posX >= 2 and ChessInfo[self.posY][self.posX - 1].chessType == ChessTypeConst.CHESS_NONE:
			#左上；向左两格，向上一格
			if self.posY >= 1:
				self.addToCurCanMovePos(self.posX - 2,self.posY - 1)
			#左下；向左两格，向下一格
			if self.posY <= 8:
				self.addToCurCanMovePos(self.posX - 2,self.posY + 1)
		#向右走
		if self.posX <= 6 and ChessInfo[self.posY][self.posX + 1].chessType == ChessTypeConst.CHESS_NONE:
			if self.posY >= 1:
				self.addToCurCanMovePos(self.posX + 2,self.posY - 1)
			if self.posY <= 8:
				self.addToCurCanMovePos(self.posX + 2,self.posY + 1)

	

redHorse1 = Horse("红马",posX = 1,posY = 9,chessType = ChessTypeConst.RED_HORSE)
redHorse2 = Horse("红马",posX = 7,posY = 9,chessType = ChessTypeConst.RED_HORSE)
blackHorse1 = Horse("黑马",posX = 1,posY = 0,chessType = ChessTypeConst.BLACK_HORSE)
blackHorse2 = Horse("黑马",posX = 7,posY = 0,chessType = ChessTypeConst.BLACK_HORSE)

class Xiang(Chess):
	def resetCanMovePos(self):
		super().resetCanMovePos()
		#左上(共有限制 and (红相限制 or 黑像限制))
		if (self.posX != 0 and self.posY != 0 and self.posY != 5):
			#中间没有遮挡
			if ChessInfo[self.posY - 1][self.posX - 1].chessType == ChessTypeConst.CHESS_NONE:
				self.addToCurCanMovePos(self.posX - 2,self.posY - 2)
		#右上(共有限制 and (红相限制 or 黑像限制))
		if (self.posX != 8 and self.posY != 0 and self.posY != 5):
			#中间没有遮挡
			if ChessInfo[self.posY - 1][self.posX + 1].chessType == ChessTypeConst.CHESS_NONE:
				self.addToCurCanMovePos(self.posX + 2,self.posY - 2)
		#左下(共有限制 and (红相限制 and 黑像限制))
		if (self.posX != 0 and self.posY != 4 and self.posY != 9 ):
			#中间没有遮挡
			if ChessInfo[self.posY + 1][self.posX - 1].chessType == ChessTypeConst.CHESS_NONE:
				self.addToCurCanMovePos(self.posX - 2,self.posY + 2)
		#右下(共有限制 and (红相限制 and 黑像限制))
		if (self.posX != 8 and self.posY != 4 and self.posY != 9 ):
			#中间没有遮挡
			if ChessInfo[self.posY + 1][self.posX + 1].chessType == ChessTypeConst.CHESS_NONE:
				self.addToCurCanMovePos(self.posX + 2,self.posY + 2)


redXiang1 = Xiang("红相",posX = 2,posY = 9,chessType = ChessTypeConst.RED_XIANG)
redXiang2 = Xiang("红相",posX = 6,posY = 9,chessType = ChessTypeConst.RED_XIANG)
blackXiang1 = Xiang("黑象",posX = 2,posY = 0,chessType = ChessTypeConst.BLACK_XIANG)
blackXiang2 = Xiang("黑象",posX = 6,posY = 0,chessType = ChessTypeConst.BLACK_XIANG)

class Shi(Chess):
	def resetCanMovePos(self):
		super().resetCanMovePos()
		#左上(共有限制 and (红相限制 or 黑像限制))
		if (self.posX != 3 and self.posY != 0 and self.posY != 7):
			self.addToCurCanMovePos(self.posX - 1,self.posY - 1)
		#右上
		if (self.posX != 5 and self.posY != 0 and self.posY != 7):
			self.addToCurCanMovePos(self.posX + 1,self.posY - 1)
		#左下
		if (self.posX != 3 and self.posY != 2 and self.posY != 9):
			self.addToCurCanMovePos(self.posX - 1,self.posY + 1)
		#右下
		if (self.posX != 5 and self.posY != 2 and self.posY != 9):
			self.addToCurCanMovePos(self.posX + 1,self.posY + 1)


redShi1 = Shi("红士",posX = 3,posY = 9,chessType = ChessTypeConst.RED_SHI)
redShi1 = Shi("红士",posX = 5,posY = 9,chessType = ChessTypeConst.RED_SHI)
blackShi1 = Shi("黑士",posX = 3,posY = 0,chessType = ChessTypeConst.BLACK_SHI)
blackShi2 = Shi("黑士",posX = 5,posY = 0,chessType = ChessTypeConst.BLACK_SHI)

class Shuai(Chess):
	def resetCanMovePos(self):
		super().resetCanMovePos()
		#上
		if (self.posY != 0 and self.posY != 7):
			self.addToCurCanMovePos(self.posX,self.posY - 1)
		#下
		if (self.posY != 2 and self.posY != 9):
			self.addToCurCanMovePos(self.posX,self.posY + 1)
		#左
		if (self.posX != 3):
			self.addToCurCanMovePos(self.posX - 1,self.posY)
		#右
		if (self.posX != 5):
			self.addToCurCanMovePos(self.posX + 1,self.posY)

redShuai = Shuai("红帅",posX = 4,posY = 9,chessType = ChessTypeConst.RED_SHUAI)
blackJiang = Shuai("黑将",posX = 4,posY = 0,chessType = ChessTypeConst.BLACK_JIANG)

class Bing(Chess):
	def resetCanMovePos(self):
		super().resetCanMovePos()
		#红兵规则
		if getPlayerSide(self.chessType) == PlayerSideConst.RED:
			if self.posY != 0:
				self.addToCurCanMovePos(self.posX,self.posY - 1)#拱卒
			#过河卒
			if self.posY <= 4:
				if self.posX != 0:
					self.addToCurCanMovePos(self.posX - 1,self.posY)#左走
				if self.posX != 8:
					self.addToCurCanMovePos(self.posX + 1,self.posY)#右走
		#黑卒
		else:
			if self.posY != 9:
				self.addToCurCanMovePos(self.posX,self.posY + 1)
			#过河卒
			if self.posY >= 5:
				if self.posX != 0:
					self.addToCurCanMovePos(self.posX - 1,self.posY)
				if self.posX != 8:
					self.addToCurCanMovePos(self.posX + 1,self.posY)

redBing1 = Bing("红兵",posX = 0,posY = 6,chessType = ChessTypeConst.RED_BING)
redBing2 = Bing("红兵",posX = 2,posY = 6,chessType = ChessTypeConst.RED_BING)
redBing3 = Bing("红兵",posX = 4,posY = 6,chessType = ChessTypeConst.RED_BING)
redBing4 = Bing("红兵",posX = 6,posY = 6,chessType = ChessTypeConst.RED_BING)
redBing5 = Bing("红兵",posX = 8,posY = 6,chessType = ChessTypeConst.RED_BING)

blackZu1 = Bing("黑卒",posX = 0,posY = 3,chessType = ChessTypeConst.BLACK_ZU)
blackZu2 = Bing("黑卒",posX = 2,posY = 3,chessType = ChessTypeConst.BLACK_ZU)
blackZu3 = Bing("黑卒",posX = 4,posY = 3,chessType = ChessTypeConst.BLACK_ZU)
blackZu4 = Bing("黑卒",posX = 6,posY = 3,chessType = ChessTypeConst.BLACK_ZU)
blackZu5 = Bing("黑卒",posX = 8,posY = 3,chessType = ChessTypeConst.BLACK_ZU)

class Pao(Chess):
	def resetCanMovePos(self):
		super().resetCanMovePos()
		tempPosX = self.posX - 1
		offSetX = -1	#向左遍历
		barrier = False
		while(True):
			if tempPosX < 0:
				tempPosX = self.posX + 1 
				barrier = False
				offSetX = 1		#碰到左边界，调头向右
				continue
			elif tempPosX > 8:	#碰到右边界，退出
				break
			tempChess = ChessInfo[self.posY][tempPosX]
			targetSide = getPlayerSide(tempChess.chessType)
			#如果该方向有跳板
			if barrier:
				if tempChess.chessType != ChessTypeConst.CHESS_NONE:
					if targetSide != curPlayerSide:
						#是敌方就加入
						self.curCanMovePos.append(tempChess)
					if offSetX == 1:
						break
					#向右调头
					tempPosX = self.posX
					barrier = False
					offSetX = 1
			#该方向无跳板
			else:
				if tempChess.chessType == ChessTypeConst.CHESS_NONE:
					self.curCanMovePos.append(NoneChess(tempPosX,self.posY))
				else:
					barrier = True	
			
			tempPosX += offSetX	

		tempPosY = self.posY - 1
		offSetY = -1	#向上遍历
		barrier = False
		while(True):
			if tempPosY < 0:
				tempPosY = self.posY + 1
				barrier = False 
				offSetY = 1	
				continue
			elif tempPosY > 9:#竖着比横着多一行
				break
			tempChess = ChessInfo[tempPosY][self.posX]
			targetSide = getPlayerSide(tempChess.chessType)
			#如果该方向有跳板
			if barrier:
				if tempChess.chessType != ChessTypeConst.CHESS_NONE:
					if targetSide != curPlayerSide:
						#是地方就加入
						self.curCanMovePos.append(tempChess)
					if offSetY == 1:
						break
					#向右调头
					tempPosY = self.posY
					barrier = False
					offSetY = 1
					
			#该方向无跳板
			else:
				if tempChess.chessType == ChessTypeConst.CHESS_NONE:
					self.curCanMovePos.append(NoneChess(self.posX,tempPosY))
				else:
					barrier = True	
			
			tempPosY += offSetY	


redPao1 = Pao("红炮",posX = 1,posY = 7,chessType = ChessTypeConst.RED_PAO)
redPao2 = Pao("红炮",posX = 7,posY = 7,chessType = ChessTypeConst.RED_PAO)
blackPao1 = Pao("黑炮",posX = 1,posY = 2,chessType = ChessTypeConst.BLACK_PAO)
blackPao2 = Pao("黑炮",posX = 7,posY = 2,chessType = ChessTypeConst.BLACK_PAO)

def DrawAllChesses():
	for i in range(len(ChessInfo)):
		for j in range(len(ChessInfo[i])):
			ChessInfo[i][j].draw()

def printChessInfo():
	for i in range(len(ChessInfo)):
		for j in range(len(ChessInfo[i])):
			tempStr = str(ChessInfo[i][j].chessType)
			if len(tempStr) == 1:
				tempStr = "0" + tempStr
			print(tempStr,end = " ")
		print("")
	print("----------------------------------")



