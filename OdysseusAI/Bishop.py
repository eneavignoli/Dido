from Piece import *

class Bishop(Piece):
    #constructors
    def __init__(self,owner,id):
        super().__init__(owner,id)
        self.type = PieceType.bishop
    
    #methods
    def possibleMoves(self,board,x,y):
        availableMoves = None
        index = 0
        
        #bishop can make 4 movements along diagonals
        
        #diagonal top left
        if y > 0 and x > 0:
            for row in reverse(y - 1, 0, -1):
                for column in reverse(x - 1, 0, -1):
                    if board.isEnemy(self.owner,column,row) or board.isEmpty(column,row):
                        availableMoves[index] = str(column)
                        index += 1
                        availableMoves[index] = str(row)
                        index += 1
        #diagonal top right
        if y > 0 and x < 7:
            for row in reverse(y - 1, 0, -1):
                for column in range(x + 1, 7, +1):
                    if board.isEnemy(self.owner,column,row) or board.isEmpty(column,row):
                        availableMoves[index] = str(column)
                        index += 1
                        availableMoves[index] = str(row)
                        index += 1
        #diagonal bottom right
        if y > 0 and x < 7:
            for row in reverse(y - 1, 0, -1):
                for column in range(x + 1, 7, +1):
                    if board.isEnemy(self.owner,column,row) or board.isEmpty(column,row):
                        availableMoves[index] = str(column)
                        index += 1
                        availableMoves[index] = str(row)
                        index += 1
        #diagonal bottom left
        if y < 7 and x > 0:
            for row in reverse(y + 1, 0, +1):
                for column in range(x - 1, 0, -1):
                    if board.isEnemy(self.owner,column,row) or board.isEmpty(column,row):
                        availableMoves[index] = str(column)
                        index += 1
                        availableMoves[index] = str(row)
                        index += 1
        
        return availableMoves