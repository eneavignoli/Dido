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
        self.chessBoard = [[0 for x in range(8)] for y in range(8)] 
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
        self.chessBoard[7][0] = Rook(leftAIRook,human)
        self.chessBoard[7][1] = Knight(leftAIKnight,human)
        self.chessBoard[7][2] = Bishop(leftAIBishop,human)
        self.chessBoard[7][3] = Queen(AIQueen,human)
        self.chessBoard[7][4] = King(AIKing,human)
        self.chessBoard[7][5] = Bishop(rightAIBishop,human)
        self.chessBoard[7][6] = Knight(rightAIKnight,human)
        self.chessBoard[7][7] = Rook(rightAIRook,human)
        self.chessBoard[6][0] = Pawn(firstAIPawn,human)
        self.chessBoard[6][1] = Pawn(secondAIPawn,human)
        self.chessBoard[6][2] = Pawn(thirdAIPawn,human)
        self.chessBoard[6][3] = Pawn(fourthAIPawn,human)
        self.chessBoard[6][4] = Pawn(fifthAIPawn,human)
        self.chessBoard[6][5] = Pawn(sixthAIPawn,human)
        self.chessBoard[6][6] = Pawn(seventhAIPawn,human)
        self.chessBoard[6][7] = Pawn(eightAIPawn,human)
    
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
        if self.chessBoard[y][x] == None:
            return True
        else:
            return False
    
    def isEnemy(self,owner,x,y):
        if self.chessBoard[y][x].getOwner != owner:
            return True
        else:
            return False
    
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
                        