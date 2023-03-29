#-----------------------------------
#callum Mcintosh
# rat class
#-----------------------------------

class Rat:
    "player"
    
    def __init__(self, x, r, c):
        self.char = x
        self.row = r
        self.column = c
        self.speed = 1
        self.food = 0

    
    #getters
    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    def getChar(self):
        return self.char

    def getSpeed(self):
        return self.speed

    def getFood(self):
        return self.food

    #setters
    def setRow(self, r):
        self.row = r

    def setColumn(self, c):
        self.column = c

    def setFood(self, f):
        self.food = f


    #other
    def toString(self):
        info = "Rat " + self.char + " at row " + str(self.row) + " and column " + str(self.column)
        info = info +  " has eaten " + str(self.food) + " meals today."
        return info
        
    def eatFood(self):
        self.food += 1

    def moveUp(self):
        self.row -= self.speed

    def moveDown(self):
        self.row += self.speed

    def moveRight(self):
        self.column += self.speed

    def moveLeft(self):
        self.column -= self.speed
        

