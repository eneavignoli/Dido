import pygame, sys
from Board import *
from Piece import *
from pygame.locals import *

def main():
    #variable that defines if it is the start of the match
    init = True
    
    #logical board
    chessBoard = Board(human)
    
    #types of squares
    WHT = 0
    BLK = 1
    CEM = 2
    #dictionary linking squares to textures
    textures = {
        WHT : pygame.image.load('img/WhiteSquare.jpg'),
        BLK : pygame.image.load('img/BlackSquare.jpg'),
        CEM : pygame.image.load('img/CemeterySquare.jpg')
        }
    #creating the board
    board = [[CEM,CEM,BLK,WHT,BLK,WHT,BLK,WHT,BLK,WHT,CEM,CEM],
             [CEM,CEM,WHT,BLK,WHT,BLK,WHT,BLK,WHT,BLK,CEM,CEM],
             [CEM,CEM,BLK,WHT,BLK,WHT,BLK,WHT,BLK,WHT,CEM,CEM],
             [CEM,CEM,WHT,BLK,WHT,BLK,WHT,BLK,WHT,BLK,CEM,CEM],
             [CEM,CEM,BLK,WHT,BLK,WHT,BLK,WHT,BLK,WHT,CEM,CEM],
             [CEM,CEM,WHT,BLK,WHT,BLK,WHT,BLK,WHT,BLK,CEM,CEM],
             [CEM,CEM,BLK,WHT,BLK,WHT,BLK,WHT,BLK,WHT,CEM,CEM],
             [CEM,CEM,WHT,BLK,WHT,BLK,WHT,BLK,WHT,BLK,CEM,CEM]]
    #useful constants
    SQUARESIZE = 40
    BOARDWIDTH = 12
    BOARDHEIGHT = 8
    
    #initialise pygame module
    pygame.init()
    #setup the display
    DISPLAYSURF = pygame.display.set_mode((BOARDWIDTH*SQUARESIZE,BOARDHEIGHT*SQUARESIZE))
    #give a name to the window
    pygame.display.set_caption('Odysseus')
    #types of pieces
    W_PAWN = pygame.image.load('img/WhitePawn.png').convert_alpha()
    W_ROOK = pygame.image.load('img/WhiteRook.png').convert_alpha()
    W_BISHOP = pygame.image.load('img/WhiteBishop.png').convert_alpha()
    W_KNIGHT = pygame.image.load('img/WhiteKnight.png').convert_alpha()
    W_QUEEN = pygame.image.load('img/WhiteQueen.png').convert_alpha()
    W_KING = pygame.image.load('img/WhiteKing.png').convert_alpha()
    B_PAWN = pygame.image.load('img/BlackPawn.png').convert_alpha()
    B_ROOK = pygame.image.load('img/BlackRook.png').convert_alpha()
    B_BISHOP = pygame.image.load('img/BlackBishop.png').convert_alpha()
    B_KNIGHT = pygame.image.load('img/BlackKnight.png').convert_alpha()
    B_QUEEN = pygame.image.load('img/BlackQueen.png').convert_alpha()
    B_KING = pygame.image.load('img/BlackKing.png').convert_alpha()
    
    #core of the program
    while True:
        #get all the user events
        for event in pygame.event.get():
            #if the user wants to quit
            if event.type == QUIT:
                #end game and close the window
                pygame.quit()
                sys.exit()
        #draw the board
        for row in range(BOARDHEIGHT):
            for column in range(BOARDWIDTH):
                DISPLAYSURF.blit(textures[board[row][column]], (column*SQUARESIZE, row*SQUARESIZE))
        if init == True:
            #place black pieces
            DISPLAYSURF.blit(B_ROOK, (2*SQUARESIZE, 0*SQUARESIZE))
            DISPLAYSURF.blit(B_KNIGHT, (3*SQUARESIZE, 0*SQUARESIZE))
            DISPLAYSURF.blit(B_BISHOP, (4*SQUARESIZE, 0*SQUARESIZE))
            DISPLAYSURF.blit(B_QUEEN, (5*SQUARESIZE, 0*SQUARESIZE))
            DISPLAYSURF.blit(B_KING, (6*SQUARESIZE, 0*SQUARESIZE))
            DISPLAYSURF.blit(B_BISHOP, (7*SQUARESIZE, 0*SQUARESIZE))
            DISPLAYSURF.blit(B_KNIGHT, (8*SQUARESIZE, 0*SQUARESIZE))
            DISPLAYSURF.blit(B_ROOK, (9*SQUARESIZE, 0*SQUARESIZE))
            DISPLAYSURF.blit(B_PAWN, (2*SQUARESIZE, 1*SQUARESIZE))
            DISPLAYSURF.blit(B_PAWN, (3*SQUARESIZE, 1*SQUARESIZE))
            DISPLAYSURF.blit(B_PAWN, (4*SQUARESIZE, 1*SQUARESIZE))
            DISPLAYSURF.blit(B_PAWN, (5*SQUARESIZE, 1*SQUARESIZE))
            DISPLAYSURF.blit(B_PAWN, (6*SQUARESIZE, 1*SQUARESIZE))
            DISPLAYSURF.blit(B_PAWN, (7*SQUARESIZE, 1*SQUARESIZE))
            DISPLAYSURF.blit(B_PAWN, (8*SQUARESIZE, 1*SQUARESIZE))
            DISPLAYSURF.blit(B_PAWN, (9*SQUARESIZE, 1*SQUARESIZE))
            #place white pieces
            DISPLAYSURF.blit(W_PAWN, (2*SQUARESIZE, 6*SQUARESIZE))
            DISPLAYSURF.blit(W_PAWN, (3*SQUARESIZE, 6*SQUARESIZE))
            DISPLAYSURF.blit(W_PAWN, (4*SQUARESIZE, 6*SQUARESIZE))
            DISPLAYSURF.blit(W_PAWN, (5*SQUARESIZE, 6*SQUARESIZE))
            DISPLAYSURF.blit(W_PAWN, (6*SQUARESIZE, 6*SQUARESIZE))
            DISPLAYSURF.blit(W_PAWN, (7*SQUARESIZE, 6*SQUARESIZE))
            DISPLAYSURF.blit(W_PAWN, (8*SQUARESIZE, 6*SQUARESIZE))
            DISPLAYSURF.blit(W_PAWN, (9*SQUARESIZE, 6*SQUARESIZE))
            DISPLAYSURF.blit(W_ROOK, (2*SQUARESIZE, 7*SQUARESIZE))
            DISPLAYSURF.blit(W_KNIGHT, (3*SQUARESIZE, 7*SQUARESIZE))
            DISPLAYSURF.blit(W_BISHOP, (4*SQUARESIZE, 7*SQUARESIZE))
            DISPLAYSURF.blit(W_QUEEN, (5*SQUARESIZE, 7*SQUARESIZE))
            DISPLAYSURF.blit(W_KING, (6*SQUARESIZE, 7*SQUARESIZE))
            DISPLAYSURF.blit(W_BISHOP, (7*SQUARESIZE, 7*SQUARESIZE))
            DISPLAYSURF.blit(W_KNIGHT, (8*SQUARESIZE, 7*SQUARESIZE))
            DISPLAYSURF.blit(W_ROOK, (9*SQUARESIZE, 7*SQUARESIZE))
        else:
            for row in range(BOARDHEIGHT):
                for column in range(BOARDWIDTH):
                    if self.chessBoard.isEmpty(column,row) == False:
                        type = self.chessBoard.getPieceType(column,row)
                        owner = self.chessBoard.isEnemy(AI,column,row)
                        #if ai
                        if owner == True:
                            if type == PieceType.rook:
                                DISPLAYSURF.blit(B_ROOK, ((column+2)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.knight:
                                DISPLAYSURF.blit(B_KNIGHT, ((column+2)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.bishop:
                                DISPLAYSURF.blit(B_BISHOP, ((column+2)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.queen:
                                DISPLAYSURF.blit(B_QUEEN, ((column+2)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.king:
                                DISPLAYSURF.blit(B_KING, ((column+2)*SQUARESIZE, row*SQUARESIZE))
                            else:
                                DISPLAYSURF.blit(B_PAWN, ((column+2)*SQUARESIZE, row*SQUARESIZE))
                        else: #if human
                            if type == PieceType.rook:
                                DISPLAYSURF.blit(W_ROOK, ((column+2)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.knight:
                                DISPLAYSURF.blit(W_KNIGHT, ((column+2)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.bishop:
                                DISPLAYSURF.blit(W_BISHOP, ((column+2)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.queen:
                                DISPLAYSURF.blit(W_QUEEN, ((column+2)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.king:
                                DISPLAYSURF.blit(W_KING, ((column+2)*SQUARESIZE, row*SQUARESIZE))
                            else:
                                DISPLAYSURF.blit(W_PAWN, ((column+2)*SQUARESIZE, row*SQUARESIZE))
                        
        #update the display
        pygame.display.update()

if __name__ == "__main__":
    main()