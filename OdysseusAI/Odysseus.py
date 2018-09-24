import pygame, sys
import serial
from Board import *
from Piece import *
from pygame.locals import *

def initialSetup():
    #variable that defines if it is the start of the match
    global initialCycle
    initialCycle = True
    
    #logical board
    global chessBoard
    chessBoard = Board(human)
    
    #colors
    global WHITE
    WHITE = (255, 255, 255)
    global BLACK
    BLACK = (0, 0, 0)
    global GREEN
    GREEN = (11, 102, 35)
    global RED
    RED = (255, 8, 0)
    
    #types of squares
    global WHT
    WHT = 0
    global BLK
    BLK = 1
    global CEM
    CEM = 2
    #dictionary linking squares to textures
    global textures
    textures = {
        WHT : pygame.image.load('img/WhiteSquare.jpg'),
        BLK : pygame.image.load('img/BlackSquare.jpg'),
        CEM : pygame.image.load('img/CemeterySquare.jpg')
        }
    #creating the board
    global board
    board = [[CEM,CEM,BLK,WHT,BLK,WHT,BLK,WHT,BLK,WHT,CEM,CEM],
            [CEM,CEM,WHT,BLK,WHT,BLK,WHT,BLK,WHT,BLK,CEM,CEM],
            [CEM,CEM,BLK,WHT,BLK,WHT,BLK,WHT,BLK,WHT,CEM,CEM],
            [CEM,CEM,WHT,BLK,WHT,BLK,WHT,BLK,WHT,BLK,CEM,CEM],
            [CEM,CEM,BLK,WHT,BLK,WHT,BLK,WHT,BLK,WHT,CEM,CEM],
            [CEM,CEM,WHT,BLK,WHT,BLK,WHT,BLK,WHT,BLK,CEM,CEM],
            [CEM,CEM,BLK,WHT,BLK,WHT,BLK,WHT,BLK,WHT,CEM,CEM],
            [CEM,CEM,WHT,BLK,WHT,BLK,WHT,BLK,WHT,BLK,CEM,CEM]]
    #useful constants
    global SQUARESIZE
    SQUARESIZE = 40
    global BOARDWIDTH
    BOARDWIDTH = 12
    global BOARDHEIGHT
    BOARDHEIGHT = 8
    
    #initialise pygame module
    pygame.init()
    #initialise font module
    pygame.font.init()
    #setup the display
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((BOARDWIDTH*SQUARESIZE,BOARDHEIGHT*SQUARESIZE),pygame.FULLSCREEN)
    #DISPLAYSURF = pygame.display.set_mode((BOARDWIDTH*SQUARESIZE,BOARDHEIGHT*SQUARESIZE))
    #give a name to the window
    pygame.display.set_caption('Odysseus')
    pygame.display.set_icon(pygame.image.load('img/odysseus_logo.png').convert_alpha())
    #get the default font
    global defaultFont
    defaultFont = pygame.font.SysFont(pygame.font.get_default_font(), 45, bold = False, italic = False)
    global littleFont
    littleFont = pygame.font.SysFont(pygame.font.get_default_font(), 30, bold = False, italic = False)
    #types of pieces
    global W_PAWN
    W_PAWN = pygame.image.load('img/WhitePawn.png').convert_alpha()
    global W_ROOK
    W_ROOK = pygame.image.load('img/WhiteRook.png').convert_alpha()
    global W_BISHOP
    W_BISHOP = pygame.image.load('img/WhiteBishop.png').convert_alpha()
    global W_KNIGHT
    W_KNIGHT = pygame.image.load('img/WhiteKnight.png').convert_alpha()
    global W_QUEEN
    W_QUEEN = pygame.image.load('img/WhiteQueen.png').convert_alpha()
    global W_KING
    W_KING = pygame.image.load('img/WhiteKing.png').convert_alpha()
    global B_PAWN
    B_PAWN = pygame.image.load('img/BlackPawn.png').convert_alpha()
    global B_ROOK
    B_ROOK = pygame.image.load('img/BlackRook.png').convert_alpha()
    global B_BISHOP
    B_BISHOP = pygame.image.load('img/BlackBishop.png').convert_alpha()
    global B_KNIGHT
    B_KNIGHT = pygame.image.load('img/BlackKnight.png').convert_alpha()
    global B_QUEEN
    B_QUEEN = pygame.image.load('img/BlackQueen.png').convert_alpha()
    global B_KING
    B_KING = pygame.image.load('img/BlackKing.png').convert_alpha()
    
    #useful images
    global RED_CROSS
    RED_CROSS = pygame.image.load('img/redCross.png').convert_alpha()

def initialOptions():
    #welcome text
    # Clear the screen and set the screen background
    DISPLAYSURF.fill(WHITE)
    #get the text object
    welcomeText = defaultFont.render('Welcome to Odysseus!', True, BLACK,WHITE)
    #print
    DISPLAYSURF.blit(welcomeText,(70, 135))
    #update screen
    pygame.display.update()
    #wait 5 seconds
    pygame.time.wait(3500)
    
    #initial menu
    flag = True
    # Clear the screen and set the screen background
    DISPLAYSURF.fill(WHITE)
    #options
    optionsText = littleFont.render('Please choose who starts the match', True, BLACK, WHITE)
    pcText = littleFont.render('PC', True, BLACK)
    humanText = littleFont.render('Human', True, BLACK)
    #wait until an option is chosen
    while flag:
        #get all the user events
        for event in pygame.event.get():
            #if the user wants to quit
            if event.type == QUIT:
                #end game and close the window
                pygame.quit()
                sys.exit()
            # This block is executed once for each MOUSEBUTTONDOWN event.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if event.pos[0] >= 90 and event.pos[0] <= 170 and event.pos[1] >= 130 and event.pos[1] <= 170:
                        return AI
                    elif event.pos[0] >= 300 and event.pos[0] <= 380 and event.pos[1] >= 130 and event.pos[1] <= 170:
                        return human
        #print
        DISPLAYSURF.blit(optionsText,(60, 70))
        #draw buttons
        pygame.draw.rect(DISPLAYSURF, GREEN,(90,130,80,40))
        pygame.draw.rect(DISPLAYSURF, BLACK,(90,130,80,40),3)
        pygame.draw.rect(DISPLAYSURF, RED,(300,130,80,40))
        pygame.draw.rect(DISPLAYSURF, BLACK,(300,130,80,40),3)
        #draw font on buttons
        DISPLAYSURF.blit(pcText,(115, 140))
        DISPLAYSURF.blit(humanText,(305, 140))
        #update screen
        pygame.display.update()

def printInitialBoard():
    #draw the board
    for row in range(BOARDHEIGHT):
        for column in range(BOARDWIDTH):
            DISPLAYSURF.blit(textures[board[row][column]], (column*SQUARESIZE, row*SQUARESIZE))
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

def printLogicalBoard():
    for row in range(BOARDHEIGHT):
        for column in range(BOARDWIDTH):
            if column < 2:
                if chessBoard.isAICemEmpty(column,row) == False:
                    type = chessBoard.getAICemPieceType(column,row)
                    if type == PieceType.rook:
                        DISPLAYSURF.blit(B_ROOK, ((column)*SQUARESIZE, row*SQUARESIZE))
                    elif type == PieceType.knight:
                        DISPLAYSURF.blit(B_KNIGHT, ((column)*SQUARESIZE, row*SQUARESIZE))
                    elif type == PieceType.bishop:
                        DISPLAYSURF.blit(B_BISHOP, ((column)*SQUARESIZE, row*SQUARESIZE))
                    elif type == PieceType.queen:
                        DISPLAYSURF.blit(B_QUEEN, ((column)*SQUARESIZE, row*SQUARESIZE))
                    elif type == PieceType.king:
                        DISPLAYSURF.blit(B_KING, ((column)*SQUARESIZE, row*SQUARESIZE))
                    else:
                        DISPLAYSURF.blit(B_PAWN, ((column)*SQUARESIZE, row*SQUARESIZE))
                elif column > 9:
                    if chessBoard.isHumanCemEmpty(column-10,row) == False:
                        type = chessBoard.getHumanCemPieceType(column-10,row)
                        if type == PieceType.rook:
                            DISPLAYSURF.blit(W_ROOK, ((column)*SQUARESIZE, row*SQUARESIZE))
                        elif type == PieceType.knight:
                            DISPLAYSURF.blit(W_KNIGHT, ((column)*SQUARESIZE, row*SQUARESIZE))
                        elif type == PieceType.bishop:
                            DISPLAYSURF.blit(W_BISHOP, ((column)*SQUARESIZE, row*SQUARESIZE))
                        elif type == PieceType.queen:
                            DISPLAYSURF.blit(W_QUEEN, ((column)*SQUARESIZE, row*SQUARESIZE))
                        elif type == PieceType.king:
                            DISPLAYSURF.blit(W_KING, ((column)*SQUARESIZE, row*SQUARESIZE))
                        else:
                            DISPLAYSURF.blit(W_PAWN, ((column)*SQUARESIZE, row*SQUARESIZE))
                else:
                    if chessBoard.isEmpty(column-2,row) == False:
                        type = chessBoard.getPieceType(column-2,row)
                        owner = chessBoard.isEnemy(AI,column-2,row)
                        #if ai
                        if owner == AI:
                            if type == PieceType.rook:
                                DISPLAYSURF.blit(B_ROOK, ((column)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.knight:
                                DISPLAYSURF.blit(B_KNIGHT, ((column)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.bishop:
                                DISPLAYSURF.blit(B_BISHOP, ((column)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.queen:
                                DISPLAYSURF.blit(B_QUEEN, ((column)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.king:
                                DISPLAYSURF.blit(B_KING, ((column)*SQUARESIZE, row*SQUARESIZE))
                            else:
                                DISPLAYSURF.blit(B_PAWN, ((column)*SQUARESIZE, row*SQUARESIZE))
                        else: #if human
                            if type == PieceType.rook:
                                DISPLAYSURF.blit(W_ROOK, ((column)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.knight:
                                DISPLAYSURF.blit(W_KNIGHT, ((column)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.bishop:
                                DISPLAYSURF.blit(W_BISHOP, ((column)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.queen:
                                DISPLAYSURF.blit(W_QUEEN, ((column)*SQUARESIZE, row*SQUARESIZE))
                            elif type == PieceType.king:
                                DISPLAYSURF.blit(W_KING, ((column)*SQUARESIZE, row*SQUARESIZE))
                            else:
                                DISPLAYSURF.blit(W_PAWN, ((column)*SQUARESIZE, row*SQUARESIZE))

def redCrossOnPiece(i_row,i_col,DISPLAYSURF):
    #put a red cross for half a second on the killed piece
    fpsClock = pygame.time.Clock()
    DISPLAYSURF.blit(RED_CROSS, ((i_col)*SQUARESIZE, i_row*SQUARESIZE))
    pygame.display.update()
    fpsClock.tick(500)

def receiveFromArduino():
    flag = True
    arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)
    while flag:
        if arduinoSerialData.inWaiting() > 0:
            myDara = arduinoSerialData.readline()
            return myData
        
def sendToArduino(message):
    arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)
    arduinoSerialData.write(message)
    
def main():
    initialSetup()
    initialOptions()
    sendToArduino('S')
    #core of the program
    while True:
        #get all the user events
        for event in pygame.event.get():
            #if the user wants to quit
            if event.type == QUIT:
                #end game and close the window
                pygame.quit()
                sys.exit()
        if initialCycle == True:
            printInitialBoard()
            init = False
        else:
            printLogicalBoard()
                        
        #update the display
        pygame.display.update()

if __name__ == "__main__":
    main()    