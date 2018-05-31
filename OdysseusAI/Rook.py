from Piece import Piece

class Rook(Piece):
    #constructors
    def __init__(self,owner,id):
        super(owner,id)
        self.type = PieceType.rook
    
    #methods
    def possibleMoves(self,board,x,y):
        availableMoves = None
        index = 0
        #straight left moves
        if x > 0:
            for i in reverse(x - 1, 0, -1):
                if board.isEnemy(self.owner,i,y):
                    availableMoves[index] = str(i)
                    index += 1
                    availableMoves[index] = str(y)
                    index += 1
                    break
                elif board.isEmpty(i,y):
                    availableMoves[index] = str(i)
                    index += 1
                    availableMoves[index] = str(y)
                    index += 1
                else:
                    break
        #straight forward moves
        if y > 0:
            for i in reverse(y - 1, 0, -1):
                if board.isEnemy(self.owner,x,i):
                    availableMoves[index] = str(x)
                    index += 1
                    availableMoves[index] = str(i)
                    index += 1
                    break
                elif board.isEmpty(i,y):
                    availableMoves[index] = str(x)
                    index += 1
                    availableMoves[index] = str(i)
                    index += 1
                else:
                    break
        #straight right moves
        if x < 7:
            for i in range(x + 1, 7, +1):
                if board.isEnemy(self.owner,i,y):
                    availableMoves[index] = str(i)
                    index += 1
                    availableMoves[index] = str(y)
                    index += 1
                    break
                elif board.isEmpty(i,y):
                    availableMoves[index] = str(i)
                    index += 1
                    availableMoves[index] = str(y)
                    index += 1
                else:
                    break
        #straight back moves
        if y < 7:
            for i in range(y + 1, 7, +1):
                if board.isEnemy(self.owner,i,y):
                    availableMoves[index] = str(x)
                    index += 1
                    availableMoves[index] = str(i)
                    index += 1
                    break
                elif board.isEmpty(i,y):
                    availableMoves[index] = str(x)
                    index += 1
                    availableMoves[index] = str(i)
                    index += 1
                else:
                    break
        
        return availableMoves