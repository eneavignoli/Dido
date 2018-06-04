from enum import Enum

#owners id
human = True
AI = False

#human pieces id
leftHumanRook = 1
leftHumanKnight = 2
leftHumanBishop = 3
humanKing = 4
humanQueen = 5
rightHumanBishop = 6
rightHumanKnight = 7
rightHumanRook = 8
firstHumanPawn = 9
secondHumanPawn = 10
thirdHumanPawn = 11
fourthHumanPawn = 12
fifthHumanPawn = 13
sixthHumanPawn = 14
seventhHumanPawn = 15
eightHumanPawn = 16

#ai pieces id
leftAIRook = 17
leftAIKnight = 18
leftAIBishop = 19
AIKing = 20
AIQueen = 21
rightAIBishop = 22
rightAIKnight = 23
rightAIRook = 24
firstAIPawn = 25
secondAIPawn = 26
thirdAIPawn = 27
fourthAIPawn = 28
fifthAIPawn = 29
sixthAIPawn = 30
seventhAIPawn = 31
eightAIPawn = 32

#chess pieces type enumeration
class PieceType(Enum):
    empty = 0
    pawn = 1
    knight = 2
    bishop = 3
    rook = 4
    queen = 5
    king = 6

class Piece(object):
    #attributes
    type = None
    
    #costructors
    def __init__(self,owner,id):
        self.owner = owner
        self.id = id
        
    #methods
    def move(self,board,x,y):
        if Moves.isValid(board,x,y):
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
    
    #override in inherited classes
    #returns an array with coordinates of piece possible moves
    def isValid(self,board,x,y):
        moves = availableMoves(board,x,y)
        _x = None
        for i in range(0,len(moves),+1):
            if i % 2 == 0:
                _x = moves[i]
            elif _x == x and moves[i] == y:
                return True
        return False
    
    #returns true if x and y of the move are valid
    def isValid(self,board,x,y):
        None
    
    #getters and setters
    def getId(self):
        return self.id
    
    def getOwner(self):
        return self.owner
    
    def getType(self):
        return self.type