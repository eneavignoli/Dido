from Board import *

class TreeNode:
    
    def __init__(self,board):
        self.chessBoard = board
        self.childList = None
        self.minimaxValue = -1
    
    def insertChild(childNode):
        self.childList.append(childNode)