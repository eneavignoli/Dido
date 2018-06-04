from Piece import *

class EmptySquare(Piece):
    
    #constructors
    def __init__(self):
        self.type = PieceType.empty 
    
    def possibleMoves(self,board,x,y):
        return None
