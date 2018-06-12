from Piece import *
from EmptySquare import EmptySquare
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from King import King
from Queen import Queen
from Pawn import Pawn

class Board:
    #attributes
    chessBoard = None
    humanCemetery = None
    AICemetery = None
    whoMoves = None
    
    #constructor
    def __init__(self,startPlayer):
        self.chessBoard = [[EmptySquare() for x in range(8)] for y in range(8)]
        self.humanCemetery = [[EmptySquare() for x in range(2)] for y in range(8)]
        self.AICemetery = [[EmptySquare() for x in range(2)] for y in range(8)]
        self.whoMoves = startPlayer
        self.setup()
        
    #methods
    def setup(self):
        #assign None to empty squares
        for row in range(2,5):
            for column in range(0,7):
                self.chessBoard[row][column] = EmptySquare()
        #assign human player pieces
        self.chessBoard[0][0] = Rook(AI,leftHumanRook)
        self.chessBoard[0][1] = Knight(AI,leftHumanKnight)
        self.chessBoard[0][2] = Bishop(AI,leftHumanBishop)
        self.chessBoard[0][3] = Queen(AI,humanQueen)
        self.chessBoard[0][4] = King(AI,humanKing)
        self.chessBoard[0][5] = Bishop(AI,rightHumanBishop)
        self.chessBoard[0][6] = Knight(AI,rightHumanKnight)
        self.chessBoard[0][7] = Rook(AI,rightHumanRook)
        self.chessBoard[1][0] = Pawn(AI,firstHumanPawn)
        self.chessBoard[1][1] = Pawn(AI,secondHumanPawn)
        self.chessBoard[1][2] = Pawn(AI,thirdHumanPawn)
        self.chessBoard[1][3] = Pawn(AI,fourthHumanPawn)
        self.chessBoard[1][4] = Pawn(AI,fifthHumanPawn)
        self.chessBoard[1][5] = Pawn(AI,sixthHumanPawn)
        self.chessBoard[1][6] = Pawn(AI,seventhHumanPawn)
        self.chessBoard[1][7] = Pawn(AI,eightHumanPawn)
        #assign ai pieces
        self.chessBoard[7][0] = Rook(human,leftAIRook)
        self.chessBoard[7][1] = Knight(human,leftAIKnight)
        self.chessBoard[7][2] = Bishop(human,leftAIBishop)
        self.chessBoard[7][3] = Queen(human,AIQueen)
        self.chessBoard[7][4] = King(human,AIKing)
        self.chessBoard[7][5] = Bishop(human,rightAIBishop)
        self.chessBoard[7][6] = Knight(human,rightAIKnight)
        self.chessBoard[7][7] = Rook(human,rightAIRook)
        self.chessBoard[6][0] = Pawn(human,firstAIPawn)
        self.chessBoard[6][1] = Pawn(human,secondAIPawn)
        self.chessBoard[6][2] = Pawn(human,thirdAIPawn)
        self.chessBoard[6][3] = Pawn(human,fourthAIPawn)
        self.chessBoard[6][4] = Pawn(human,fifthAIPawn)
        self.chessBoard[6][5] = Pawn(human,sixthAIPawn)
        self.chessBoard[6][6] = Pawn(human,seventhAIPawn)
        self.chessBoard[6][7] = Pawn(human,eightAIPawn)
    
    #returns array of coordinates, elem 0 contains cemetery or board
    def find(self,type,owner,id):
        coordinates[0] = 0
        
        #control if in board
        for row in range(0,7):
            for column in range(0,7):
                if self.chessBoard[row][column].getId == id:
                    coordinates[1] = column
                    coordinates[2] = row
                    return coordinates
                
        coordinates[0] = 1
        
        #control if in cemetery
        if owner == human:
            for row in range(0,7):
                for column in range(0,1):
                    if self.humanCemetery[row][column].getId == id:
                        coordinates[1] = column
                        coordinates[2] = row
                        return coordinates
        else:
            for row in range(0,7):
                for column in range(0,1):
                    if self.AICemetery[row][column].getId == id:
                        coordinates[1] = column
                        coordinates[2] = row
                        return coordinates
    
    def empty(self,x,y):
        self.chessBoard[y][x] = None
        
    def assign(self,piece,x,y):
        self.chessBoard[y][x] = piece
    
    def isEmpty(self,x,y):
        if self.chessBoard[y][x] == None or self.chessBoard[y][x].getType() == PieceType.empty:
            return True
        else:
            return False
    
    def isHumanCemEmpty(self,x,y):
        if self.humanCemetery[y][x] == None or self.humanCemetery[y][x].getType() == PieceType.empty:
            return True
        else:
            return False
    
    def isAICemEmpty(self,x,y):
        if self.AICemetery[y][x] == None or self.AICemetery[y][x].getType() == PieceType.empty:
            return True
        else:
            return False
    
    def isEnemy(self,owner,x,y):
        if self.chessBoard[y][x].getOwner() != owner:
            return True
        else:
            return False
    
    def isHumanCemEnemy(self,owner,x,y):
        if self.humanCemetery[y][x].getOwner() != owner:
            return True
        else:
            return False
    
    def isAICemEnemy(self,owner,x,y):
        if self.AICemetery[y][x].getOwner() != owner:
            return True
        else:
            return False
    
    def getHumanCemPieceType(self,x,y):
        return self.humanCemetery[y][x].getType()
    
    def getAICemPieceType(self,x,y):
        return self.AICemetery[y][x].getType()
    
    def getPieceType(self,x,y):
        return self.chessBoard[y][x].getType()
        
    #moves piece to the cemetery
    def capturePiece(self,x,y):
        if self.chessBoard[y][x].getOwner == human:
            for row in range(0,7):
                for column in range(0,1):
                    if self.humanCemetery[row][column] == None:
                        self.humanCemetery[row][column] = self.chessBoard[y][x]
                        self.chessBoard[y][x] = None
                        return
        else:
            for row in range(0,7):
                for column in range(0,1):
                    if self.AICemetery[row][column] == None:
                        self.AICemetery[row][column] = self.chessBoard[y][x]
                        self.chessBoard[y][x] = None
                        return
    
    #evaluation function for minimax
    def eval(self):
        minimaxValue = 0
        #evaluating ai pieces
        for row in range(8):
            for column in range(8):
                if self.chessBoard[row][column].isEmpty == False:
                    if self.chessBoard[row][column].getOwner() == False:
                        minimaxValue = minimaxValue + self.chessBoard[row][column].getType()
                    else:
                        minimaxValue = minimaxValue - self.chessBoard[row][column].getType()
        
        return minimaxValue