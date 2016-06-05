import pyautogui as mouse
from PIL import Image, ImageOps, ImageGrab
import random, time, math
#Requires the pyautogui and pillow(PIL) library
"""
Plays TicTacToe on a 1920x1080 monitor, normal (100% zoom), at playtictactoe.org
"""

tlX = 760 #coordinates of the center of the top left square
tlY = 300
black = (0,0,0) #preset variables for colors
white = (255,255,255)
mainboard = [0,0,0,0,0,0,0,0,0] #intializes board for first checks
#------------------------------------------------------------------------------------------------------------------------------------------------------
def checkempty(board):
    """takes a board and returns a list of all the positions of the 0's (empty slots)"""
    empty = [] #initializes empty list to fill
    for item in range(9): # go through each item

        if board[item] == 0: #if the space is a 0
            empty += [item] #add the coordinates to the empty list

    return empty
#------------------------------------------------------------------------------------------------------------------------------------------------------
def pictoboard():
    """takes a picture of the screen and returns a board matching the screen"""
    board = [0,0,0,0,0,0,0,0,0] #initializes a board to edit
    im = ImageGrab.grab() #takes a picture
    
    for item in range(9): #goes through each space
        
        centerX = tlX+(item%3)*200 #checks pixels in square according to square it is checking
        centerY = tlY+(math.floor(item/3))*200

        checkX = im.getpixel((centerX,centerY)) #checks center pixel to see if it is an x
        checkO = im.getpixel((centerX-50,centerY)) #checks edge pixel to see if it is an o

        if checkX == white: board[item] = 1 #edits board if there is an x to 1
        elif checkO == white: board[item] = 2 #edits board if there is an o to 2

        else: board[item] = 0 #keeps empty spaces 0
    return board
#------------------------------------------------------------------------------------------------------------------------------------------------------
def over(board):
    """takes a board and checks if someone has won
    returns 1 for a win, -1 for a loss, 0 for a tie, or false if the game is still going"""
    empty = checkempty(board) #creates list of empties for tie checking

    #if 3 in a row are ours
    if (board[0]==board[1]==board[2]==1 or board[3]==board[4]==board[5]==1 or board[6]==board[7]==board[8]==1 or board[0]==board[3]==board[6]==1 or 
    board[1]==board[4]==board[7]==1 or board[2]==board[5]==board[8]==1 or board[0]==board[4]==board[8]==1 or board[2]==board[4]==board[6]==1):
        print('----------Win----------')
        return 1

    #if 3 in a row are theirs
    elif (board[0]==board[1]==board[2]==2 or board[3]==board[4]==board[5]==2 or board[6]==board[7]==board[8]==2 or board[0]==board[3]==board[6]==2 or 
      board[1]==board[4]==board[7]==2 or board[2]==board[5]==board[8]==2 or board[0]==board[4]==board[8]==2 or board[2]==board[4]==board[6]==2):
        print('----------Loss----------')
        print(board)
        return -1

    #if the board is full
    elif len(empty) == 0:
        print('----------Tie----------')
        return 0

    #if no one has won, and the board still has spaces
    else:
        return 'false'
#------------------------------------------------------------------------------------------------------------------------------------------------------
def movefinder(board):
    """pass it a board of the current game and it will look at all the possibilities"""

    dupboard = board
    dupempty = checkempty(board)
    for item in dupempty:
        dupboard[item] = 1
        if over(dupboard) == 1:
            print('winning')
            return item
        else:
            dupboard[item] = 0
    for item in dupempty:
        dupboard[item] = 2
        if over(dupboard) == -1:
            print('blocking')
            return item
        else:
            dupboard[item] = 0
    print('random')
    return random.choice(dupempty)
      
              
def possibilities(board,player):
    """p"""
    return true

while 1 == 1:

    mainboard = pictoboard() 

    while over(mainboard) == 'false':

        mainboard = pictoboard()       
        empty = checkempty(mainboard)
        
        play = movefinder(mainboard) #pick a random one in empty
        mouse.click(tlX+(play%3)*200,tlY+(math.floor(play/3))*200) #click on that spot
        time.sleep(1)
        mainboard = pictoboard()

    mouse.click(tlX,tlY)
 
def playmaker():
    score = []
    board = pictoboard()
    empty = checkempty(board)
    for item in empty:
        score.append([item,0])
        board = pictoboard()
        empty = checkempty(board)
        board[item] = 1
        if over != 'false':
            return 'true'
                

			
    
    





                
   
                
                
            


