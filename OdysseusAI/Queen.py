from Piece import *

class Queen(Piece):
    #constructors
    def __init__(self,owner,id):
        super().__init__(owner,id)
        self.type = PieceType.queen