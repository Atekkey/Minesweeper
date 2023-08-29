import random
import math
class Board():
    def __init__(self, size, mine):
        self.board = [[0 for i in range(size[0])] for j in range(size[1])]
        self.mine = mine
    def __str__(self):
        temp = ""
        for row in self.board:
            for col in row:
                temp += " " + str(col)
            temp += "\n"
        temp += "Mines : " + str(self.mine)
        return temp

#MAIN
myBoard = Board((2,2), 10)
print(myBoard)
