#Rand # of mines
#Rand position of mines (try tuples and sets of tuples)
#Create board
#Assign mines
#!!Assign numbers!!

import random
class Board():

    def __init__(self, size, mine): #Constructor. If mine<=0, gives a random mine#
        self.gameOver = False
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

    def main(self):
        self.plant()
        self.populate()
        while(not self.gameOver):
            print(self.showShown())
            self.ask()
            self.checkWin() #Win is outside, Loss terminates program
        print(self)
        print("You won!")

#MAIN
myBoard = Board(size = (10,10), mine = 15)
myBoard.main()
