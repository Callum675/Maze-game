#-------------------------------------------------------------------------------
# maze
# callum mcintosh
#-------------------------------------------------------------------------------

class Maze:
    """ A 2D maze. """

    def __init__(self):
        """the maze constructor
	(none) -> none
        start by declaring attributes"""
        self.maze = [['#','#','#','#','#','#','#'],
                     ['#',' ',' ',' ',' ',' ','#'],
                     ['#',' ','#','#','#',' ','#'],
                     ['#','#','#','@',' ',' ','#'],
                     ['#',' ','#',' ','#',' ','#'],
                     ['#',' ',' ',' ','#',' ','#'],
                     ['#','#','#','#','#','#','#']]
        self.food = 1
        self.width = 7
        self.height = 7

    #getters
    def getCharAtPos(self, row, column):
        return self.maze[row][column]

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width
    
    def getFood(self):
        return self.food

    #other
    def toString(self):
        """prints out the maze
	(none) -> none"""
        printme = ""
        for i in range (0,len(self.maze)):
            for j in self.maze[i]:
                printme = printme + j
            printme = printme + "\n"
        return printme
    
    def placeRat (self, rat_char, row, column):
        """places a rat at a specified row and column in the maze
	(char, int, int) -> none"""
        self.maze[row][column] = rat_char
            
    def clearAtPos(self, row, column):
        self.maze[row][column] = " "

    def eatFood(self):
        self.food -= 1


    def goToLevel2(self):
        self.maze = [['#','#','#','#','#','#','#'],
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#',' ','#',' ','#','@','#'],
                     ['#',' ',' ',' ','#','#','#'],
                     ['#',' ','#',' ','#','@','#'],
                     ['#','@','#',' ',' ',' ','#'],
                     ['#','#','#','#','#','#','#']]
        self.food = 3

        
        





    
