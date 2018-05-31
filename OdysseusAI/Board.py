from Piece import Piece
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
    
    #constructor
    def __init__(self):
        self.chessBoard = Piece[8][8]
        
    #methods
    def setup(self):
        #assign None to empty squares
        for row in range(2,5):
            for column in range(0,7):
                self.chessBoard[row][column] = None
        #assign human player pieces
        self.chessBoard[0][0] = Piece(Rook(leftHumanRook,human))
        self.chessBoard[0][1] = Piece(Knight(leftHumanKnight,human))
        self.chessBoard[0][2] = Piece(Bishop(leftHumanBishop,human))
        self.chessBoard[0][3] = Piece(Queen(humanQueen,human))
        self.chessBoard[0][4] = Piece(King(humanKing,human))
        self.chessBoard[0][5] = Piece(Bishop(rightHumanBishop,human))
        self.chessBoard[0][6] = Piece(Knight(rightHumanKnight,human))
        self.chessBoard[0][7] = Piece(Rook(rightHumanRook,human))
        self.chessBoard[1][0] = Piece(Pawn(firstHumanPawn,human))
        self.chessBoard[1][1] = Piece(Pawn(secondHumanPawn,human))
        self.chessBoard[1][2] = Piece(Pawn(thirdHumanPawn,human))
        self.chessBoard[1][3] = Piece(Pawn(fourthHumanPawn,human))
        self.chessBoard[1][4] = Piece(Pawn(fifthHumanPawn,human))
        self.chessBoard[1][5] = Piece(Pawn(sixthHumanPawn,human))
        self.chessBoard[1][6] = Piece(Pawn(seventhHumanPawn,human))
        self.chessBoard[1][7] = Piece(Pawn(eightHumanPawn,human))
        #assign ai pieces
        self.chessBoard[7][0] = Piece(Rook(leftAIRook,AI))
        self.chessBoard[7][1] = Piece(Knight(leftAIKnight,AI))
        self.chessBoard[7][2] = Piece(Bishop(leftAIBishop,AI))
        self.chessBoard[7][3] = Piece(Queen(AIQueen,AI))
        self.chessBoard[7][4] = Piece(King(AIKing,AI))
        self.chessBoard[7][5] = Piece(Bishop(rightAIBishop,AI))
        self.chessBoard[7][6] = Piece(Knight(rightAIKnight,AI))
        self.chessBoard[7][7] = Piece(Rook(rightAIRook,AI))
        self.chessBoard[6][0] = Piece(Pawn(firstAIPawn,AI))
        self.chessBoard[6][1] = Piece(Pawn(secondAIPawn,AI))
        self.chessBoard[6][2] = Piece(Pawn(thirdAIPawn,AI))
        self.chessBoard[6][3] = Piece(Pawn(fourthAIPawn,AI))
        self.chessBoard[6][4] = Piece(Pawn(fifthAIPawn,AI))
        self.chessBoard[6][5] = Piece(Pawn(sixthAIPawn,AI))
        self.chessBoard[6][6] = Piece(Pawn(seventhAIPawn,AI))
        self.chessBoard[6][7] = Piece(Pawn(eightAIPawn,AI))
    
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
                        