from Piece import Piece

class Pawn(Piece):
    stillFixed = None
    
    #constructors
    def __init__(self,owner,id):
        super(owner,id)
        self.type = PieceType.pawn
        self.stillFixed = True
    
    #methods
    def move(self,board,x,y):
        #useful to identify the first move of the pawn
        if self.stillFixed:
            self.stillFixed = False
            
        if possibleMoves(board,x,y):
            if board.isEmpty(x,y):
                #find old x,y of the piece
                oldLocation = board.find(self.type,self.owner,self.typeNum)
                #empty old x,y
                board.empty(oldLocation[0],oldLocation[1])
                #move to the new position
                board.assign(self,x,y)
                return True
                
            else:
                #move enemy piece to the cemetery
                board.capturePiece(x,y)
                #move pawn to new position
                board.assign(self,x,y)
                return True
        else:
            return False   
    
    def possibleMoves(self,board,x,y):
        availableMoves = None
        index = 0
        if self.owner == AI:
            #two squares forward if it's the first move
            if self.stillFixed:
                if board.isEmpty(x,y-2):
                    availableMoves[index] = str(x)
                    index += 1
                    availableMoves[index] = str(y-2)
                    index += 1
            elif y > 0 and board.isEmpty(x,y-1):
                availableMoves[index] = str(x)
                index += 1
                availableMoves[index] = str(y-1)
                index += 1
        
            #higher left corner
            if x > 0 and y > 0 and board.isEnemy(self.owner,x - 1,y - 1):
                availableMoves[index] = str(x - 1)
                index += 1
                availableMoves[index] = str(y - 1)
                index += 1
            #higher right corner
            if x < 7 and y > 0 and board.isEnemy(self.owner,x + 1,y - 1):
                availableMoves[index] = str(x + 1)
                index += 1
                availableMoves[index] = str(y - 1)
                index += 1
        else:
            #two squares forward if it's the first move
            if self.stillFixed:
                if board.isEmpty(x,y+2):
                    availableMoves[index] = str(x)
                    index += 1
                    availableMoves[index] = str(y+2)
                    index += 1
            elif y < 7 and board.isEmpty(x,y+1):
                availableMoves[index] = str(x)
                index += 1
                availableMoves[index] = str(y+1)
                index += 1
        
            #bottom left corner
            if x > 0 and y < 7 and board.isEnemy(self.owner,x - 1,y + 1):
                availableMoves[index] = str(x - 1)
                index += 1
                availableMoves[index] = str(y + 1)
                index += 1
            #bottom right corner
            if x < 7 and y > 7 and board.isEnemy(self.owner,x + 1,y + 1):
                availableMoves[index] = str(x + 1)
                index += 1
                availableMoves[index] = str(y + 1)
                index += 1
        #return array of possible moves
        return availableMoves