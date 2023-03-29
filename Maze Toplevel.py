#------------------
# maze toplevel
# callum mcintosh
#-----------------


#imports
from maze import Maze
from Rat import Rat
m = Maze()
r = Rat('R', 1, 1)


#interface
def menu():
    print("Controls")
    print("q: quit game")
    print("w: up")
    print("s: down")
    print("a: left")
    print("d: right")
    
#functions
def load():
    "loads the game"
    menu()
    m.placeRat("R", 1, 1)
    print(m.toString())
    main()

def moveUp():
    x = m.getCharAtPos(r.getRow()-1, r.getColumn())
    if (x == "#"):
        print("This is a wall")
    else:
        if (x == "@"):
            print("yum yum yum")
            r.eatFood()
            m.eatFood()
        m.clearAtPos(r.getRow(), r.getColumn())
        r.moveUp()
        m.placeRat(r.getChar(), r.getRow(), r.getColumn())
    print(m.toString())
    print (r.toString())

def moveDown():
    x = m.getCharAtPos(r.getRow()+1, r.getColumn())
    if x == "#":
        print("This is a wall")
    else:
        if x == "@":
            print("yum yum yum")
            r.eatFood()
            m.eatFood()
        m.clearAtPos(r.getRow(), r.getColumn())
        r.moveDown()
        m.placeRat(r.getChar(), r.getRow(), r.getColumn())
    print(m.toString())
    print (r.toString())

def moveLeft():
    x = m.getCharAtPos(r.getRow(), r.getColumn() -1)
    if (x == "#"):
        print("This is a wall")
    else:
        if (x == "@"):
            print("yum yum yum")
            r.eatFood()
            m.eatFood()
        m.clearAtPos(r.getRow(), r.getColumn())
        r.moveLeft()
        m.placeRat(r.getChar(), r.getRow(), r.getColumn())
    print(m.toString())
    print (r.toString())

def moveRight():
    x = m.getCharAtPos(r.getRow(), r.getColumn() +1)
    if (x == "#"):
        print("This is a wall")
    else:
        if (x == "@"):
            print("yum yum yum")
            r.eatFood()
            m.eatFood()
        m.clearAtPos(r.getRow(), r.getColumn())
        r.moveRight()
        m.placeRat(r.getChar(), r.getRow(), r.getColumn())
    print(m.toString())
    print (r.toString())

def main():
    "main program"
    #input
    n = str(input("input->"))
    #controls
    if (n == "w"):
        moveUp()
    elif (n == "s"):
        moveDown()
    elif (n == "a"):
        moveLeft()
    elif (n == "d"):
        moveRight()
    elif (n == 6):
        print ("program will quit")
    else:
        print("please enter a vaild inputfrom the menu")
        
    #exit
    while (n == "q"):
        exit()
    else:
        #reruns the program
        main()

#run load function
load()

