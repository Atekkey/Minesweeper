#Rand # of mines
#Rand position of mines (try tuples and sets of tuples)
#Create board
#Assign mines
#!!Assign numbers!!

import random
class Board():

    def __init__(self, size, mine): #Constructor. If mine<=0, gives a random mine#
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
        temp = ""
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
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
        #Iterate thru the X's or thru the 0's?
        #Edge cases (literally)

        #0 iter
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if(self.board[row][col] == "X"):
                    continue
                myTuples = self.validTuples((row, col))
                for k in myTuples:
                    if(self.board[k[0]][k[1]] == "X"):
                        self.board[row][col] += 1
    def main(self):
        self.plant()
        self.populate()
        print(self)

#MAIN
myBoard = Board((10,10), 0)
myBoard.main()
