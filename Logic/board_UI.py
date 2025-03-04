#Rand # of mines
#Rand position of mines (try tuples and sets of tuples)
#Create board
#Assign mines
#!!Assign numbers!!

import random
import sys
import keyboard as kb

try:
    nums = sys.argv[1:]
    mainSize = [int(nums[0]), int(nums[1])]
    mainSize[0] = min(max(mainSize[0], 3), 20)
    mainSize[1] = min(max(mainSize[1], 3), 12)

except:
    mainSize = [10, 10]


class Board():

    def __init__(self, size, mine): #Constructor. If mine<=0, gives a random mine#
        self.gameOver = False
        self.isFlag = [[False for i in range(size[0])] for j in range(size[1])]
        self.chainedList = []
        self.board = [[0 for i in range(size[0])] for j in range(size[1])]
        self.shown = [[False for i in range(size[0])] for j in range(size[1])] #Visibility mask
        if(mine <= 0):
            self.mine = random.randint(10 * 2, int((len(self.board) - 1) * (len(self.board[0]) - 1) / 2))
        else:
            self.mine = mine

    def __str__(self): #Prints out board (ex: print(myBoard))
        temp = ""
        for row in self.board:
            for col in row:
                temp += " " + str(col)
            temp += "\n"
        temp += "Mines : " + str(self.mine)
        return temp
    
    def showShown(self): #Shows what is visible to player
        temp = "# "
        for row in range(len(self.board)):
            if(row == 0):
                for col in range(len(self.board[row])):
                    temp += str(col) + "|"
                temp += "\n"
            for col in range(len(self.board[row])):
                if(col == 0):
                    temp += str(row) + "-"
                if(self.shown[row][col] == True):
                    temp += str(self.board[row][col]) + " "
                else:
                    temp += "■" + " "
            temp += "\n"
        return temp
    
    def randTuple(self):
        temp = (random.randint(0, len(self.board) - 1), random.randint(0, len(self.board[0]) - 1))
        return temp
    
    def plant(self): #Plant mines
        iter = 0
        while iter < self.mine :
            temp = self.randTuple()
            if(self.board[temp[0]][temp[1]] != "X"):
                self.board[temp[0]][temp[1]] = "X"
                iter += 1
    
    def validTuples(self, myRowCol):
        row, col = myRowCol[0], myRowCol[1]
        rowMax, colMax = len(self.board), len(self.board[0])
        myList = []
        if(col-1 >= 0): #3/8
            myList.append((row, col-1))
            if(row-1 >= 0):
                myList.append((row-1, col-1))
            if(row+1 < rowMax):
                myList.append((row+1, col-1))
        if(col+1 < colMax): #6/8
            myList.append((row, col+1))
            if(row-1 >= 0):
                myList.append((row-1, col+1))
            if(row+1 < rowMax):
                myList.append((row+1, col+1))
        if(row-1 >= 0):
            myList.append((row-1, col))
        if(row+1 < rowMax):
            myList.append((row+1, col))
        return myList
            
    
    def populate(self): #Populate the numbers
        print(" ")
        #Iterate thru 0's
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if(self.board[row][col] == "X"):
                    continue
                myTuples = self.validTuples((row, col))
                for k in myTuples:
                    if(self.board[k[0]][k[1]] == "X"):
                        self.board[row][col] += 1

    def chain(self, myRowCol):
        showList = self.validTuples((myRowCol))
        for k in showList:
            if (k in self.chainedList):
                continue
            self.chainedList.append(k)
            row, col = k[0], k[1]
            self.shown[row][col] = True
            if(self.board[row][col] == 0):
                self.chain((row,col))

    def chord(self, myRowCol):
        toCheck = self.validTuples((myRowCol))
        for tup in toCheck:
            if(self.isFlag[tup[0]][tup[1]]):
                continue
            else:
                self.shown[tup[0]][tup[1]] = True
                if(self.board[tup[0]][tup[1]] == 0):
                    self.chain(tup)
    
    def ask(self):
        got = input("Give a row and col in form #x# \n")
        got = got.split("x")
        row, col = int(got[0]), int(got[1])
        self.shown[row][col] = True
        if(self.board[row][col] == "X"): #LOSE HERE
            self.gameOver = True
            print(self)
            print("You Lost!")
            exit(1)
        elif(self.board[row][col] == 0):
            self.chain((row,col))

    def checkWin(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if(self.board[row][col] != "X" and self.shown[row][col] == False):
                    self.gameOver = False
                    return
        self.gameOver = True
        return

    def setUp(self):
        self.plant()
        self.populate()

#MAIN
def main():
    myBoard = Board(size = mainSize, mine = mainSize[0]*mainSize[1]//8)

    myBoard.setUp()


    """
    USER INTERFACE
    """

    import PySimpleGUI as sg
    sg.theme('LightBlue1') 

    layout = [
            [sg.Text("MINESWEEPER", key = "MS", text_color="black", font=("Arial", 15, ), )],
            [[sg.Button("", size = (2,2), button_color = "black on orange", key = (i,j)) for j in range(mainSize[0])] for i in range(mainSize[1])],
            [sg.Button("Restart", button_color = "white on blue", size=(10,2), key = "restart" ), sg.Button("Exit", button_color = "white on blue", size=(10,2), key = "exit" ), sg.Button("Flag Mode", button_color = "white on blue", key = "FM", size=(10,2))]
            ]

    window = sg.Window('Minesweeper', layout, size = ((mainSize[0]*80,mainSize[1]*80 )), element_justification='c')

    won = True
    flagMode = False
    while True:
        event, values = window.read()
        row, col = event[0], event[1]

        if event == sg.WIN_CLOSED or event == "exit": # Player Leaves Game
            window.close()
            return False
        
        if event == "restart": # Player Leaves Game
            window.close()
            return True

        if(event == "FM"): # Player Clicked Flag Mode Button
            flagMode = not flagMode
            if(flagMode):
                window["FM"].update(button_color = "black on green")
            else:
                window["FM"].update(button_color = "white on blue")
            continue


        if(flagMode): # Player Places Flag
            if myBoard.shown[row][col]: # Cannot put flag
                continue
            if(myBoard.isFlag[row][col] == False):
                window[event].update(image_filename = "flag1.png",  image_subsample = 17)
                myBoard.isFlag[row][col] = True
            else:
                window[event].update(image_filename = "clear1.png",  image_subsample = 50)
                myBoard.isFlag[row][col] = False
            continue

        needUpdate = False

        if(myBoard.isFlag[row][col] == True): # Is flagged:
            window[event].update(image_filename = "clear1.png",  image_subsample = 50)

        if(myBoard.board[row][col] == 0): # Chain 0 Logic
            myBoard.shown[row][col] = True
            myBoard.chain((row,col))
            needUpdate = True
        elif(myBoard.shown[row][col] == True): # Chord Chain Logic
            myBoard.chord((row,col))
            needUpdate = True
        myBoard.shown[row][col] = True
        if needUpdate:
            for i in range(mainSize[1]):
                for j in range(mainSize[0]):
                    if (myBoard.shown[i][j]):
                        window[(i,j)].update(myBoard.board[i][j], button_color = "black on yellow")
                        #window[(i,j)].update(image_filename = "clear1.png",  image_subsample = 50)
                        if(myBoard.board[i][j] == "X"):
                            window[(i,j)].update(button_color = "Red", image_filename = "mineB1.png", image_subsample = 20 )
                            won = False
                            break
        # Single Click
        i,j = row, col
        window[(i,j)].update(myBoard.board[i][j], button_color = "black on yellow")
        if(myBoard.board[i][j] == "X"):
            window[(i,j)].update(button_color = "Red", image_filename = "mineB1.png", image_subsample = 20 )
            won = False
            break
        myBoard.checkWin()
        if(not won or myBoard.gameOver):
            break

    for i in range(mainSize[1]):
        for j in range(mainSize[0]):
            window[(i,j)].update(myBoard.board[i][j])
            if(myBoard.board[i][j] == "X"):
                window[(i,j)].update(button_color = "Red", image_filename = "mineB1.png", image_subsample = 20 )
    myBoard.checkWin()
    if(not won):
        window["MS"].update("YOU LOST!!")
        window["MS"].update(text_color = "red")
    if(myBoard.gameOver):
        window["MS"].update("YOU WON!!")
        window["MS"].update(text_color = "green")

    while True:
        event, values = window.read() # Wait for any click to leave
        if event == "exit" or event == sg.WIN_CLOSED:
            window.close()
            return False
        if event == "restart":
            window.close()
            return True
    # END MAIN


playAgain = True
while playAgain:
    try:
        playAgain = main()
    except Exception as e:
        print("Quit on ", e)
        playAgain = False