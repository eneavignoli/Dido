from Piece import Piece

class Knight(Piece):
    #constructors
    def __init__(self,owner,id):
        super(owner,id)
        self.type = PieceType.knight
    
    #methods
    def possibleMoves(self,board,x,y):
        availableMoves = None
        index = 0
        #normally knights can do 8 possible L movements, so there are 8 if to verify them
        if x > 1 and y > 0 and (board.isEmpty(self.owner,x-1,y-2) or board.isEnemy(self.owner,x-1,y-2)):
            availableMoves[index] = str(x-1)
            index += 1
            availableMoves[index] = str(y-2)
            index += 1
        if x > 0 and y > 1 and (board.isEmpty(self.owner,x-2,y-1) or board.isEnemy(self.owner,x-2,y-1)):
            availableMoves[index] = str(x-2)
            index += 1
            availableMoves[index] = str(y-1)
            index += 1
        if x < 7 and y > 1 and (board.isEmpty(self.owner,x+1,y-2) or board.isEnemy(self.owner,x+1,y-2)):
            availableMoves[index] = str(x+1)
            index += 1
            availableMoves[index] = str(y-2)
            index += 1
        if x < 6 and y > 0 and (board.isEmpty(self.owner,x+2,y-1) or board.isEnemy(self.owner,x+2,y-1)):
            availableMoves[index] = str(x+2)
            index += 1
            availableMoves[index] = str(y-1)
            index += 1
        if x < 6 and y < 7 and (board.isEmpty(self.owner,x+2,y+1) or board.isEnemy(self.owner,x+2,y+1)):
            availableMoves[index] = str(x+2)
            index += 1
            availableMoves[index] = str(y+1)
            index += 1
        if x < 7 and y < 6 and (board.isEmpty(self.owner,x+1,y+2) or board.isEnemy(self.owner,x+1,y+2)):
            availableMoves[index] = str(x+1)
            index += 1
            availableMoves[index] = str(y+2)
            index += 1
        if x > 0 and y < 6 and (board.isEmpty(self.owner,x-1,y+2) or board.isEnemy(self.owner,x-1,y+2)):
            availableMoves[index] = str(x-1)
            index += 1
            availableMoves[index] = str(y+2)
            index += 1
        if x > 1 and y < 7 and (board.isEmpty(self.owner,x-2,y+1) or board.isEnemy(self.owner,x-2,y+1)):
            availableMoves[index] = str(x-2)
            index += 1
            availableMoves[index] = str(y+1)
            index += 1
            
        return availableMoves