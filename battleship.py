import os
import random

userPrimaryGrid = [['.' for x in range(11)] for y in range(11)]
userTargetGrid = [['.' for x in range(11)] for y in range(11)]
computerPrimaryGrid = [['.' for x in range(11)] for y in range(11)]
computerTargetGrid = [['.' for x in range(11)] for y in range(11)]
SHIPS = [["Carrier", 5], ["Battleship", 4], ["Cruiser", 3], ["Submarine", 3], ["Destroyer", 2]]

def createMap(grid):
    #blank top left
    grid[0][0] = "  "
    #create alpha column header
    letter = 64
    for col in range(1, 11):
        grid[0][col] = chr(letter + col)
    #create numeric row header
    for row in range(1, 11):
        grid[row][0] = "{:02d}".format(row)
    

def printScreen(primaryMap, targetMap):
    print('      TARGET GRID')
    for row in targetMap:
        for value in row:
            print(str(value) + " ", end='')
        print('')
    print('')
    print('      PRIMARY GRID')
    for row in primaryMap:
        for value in row:
            print(str(value) + " ", end='')
        print('')
        
def placeShips(grid):
    for ship in SHIPS:
        while True:
            name, length = ship[0], ship[1]
            #prompt for ship's coordinates
            while True:
                shipHead = input("Where would you like to place the " + name + " (" + str(length) + " spaces)?  Use the format LETTERNUMBER (e.g. B5): ")
                try:
                    #assign to x and y coords
                    col = ord(shipHead.upper()[:1]) - 64
                    row = int(shipHead[1:])
                except:
                    print('Invalid coordinates')
                if 0 < col < 11 and 0 < row < 11:
                    break
                print('Invalid coordinates')
            #get ship direction
            while True:
                print("col= " + str(col) + " row= " + str(row))
                dir = input("Down or Right: ").lower()
                if dir == "right" or dir == "down":
                    break
                print('Invalid direction')
            if shipOnFreeSpace(col, row, length, grid, dir):
                break
            else:
                print("Ship is not on a valid space, please try again")
        placeShip(col, row, length, grid, dir)
        printScreen(grid, userTargetGrid)
                    
#if each space we place a ship is not free or valid, return false
def shipOnFreeSpaces(col, row, len, grid, dir):
    print("in")
    if dir == "down":
        print("2")
        try:
            for i in range(len):
                print(' row= ' + str(row + i) + 'col= ' + str(col) + ' space= ' + str(grid[row+i][col]))
                if grid[row + i][col] != '.':
                    return False
        except:
            return False
    elif dir == "right":
        try:
            for i in range(len):
                print(' row= ' + str(row) + 'col= ' + str(col+i) + ' space= ' + str(grid[row][col+i]))
                if grid[row][col + i] != '.':
                    return False
        except:
            return False
    return True

def placeShip(col, row, len, grid, dir):
    if dir == "down":
        for i in range(len):
            grid[row + i][col] = u"\u25A0"
    elif dir == "right":
        for i in range(len):
            grid[row][col + i] = u"\u25A0"

def createRandomGrid(grid):
    for ship in SHIPS:
        length = ship[1]
        while True:
            col = random.randrange(1,11)
            row = random.randrange(1,11)
            if random.randrange(2) == 0:
                dir = "down"
            else:
                dir = "right"
                print("col= " + str(col) + " row= " + str(row) + "dir= " + str(dir))
            if shipOnFreeSpaces(col, row, length, grid, dir):
                break
        placeShip(col, row, length, grid, dir)
        
        
#game
    #turn
        #player guesses space
        #if correct, write X on computerPrimaryGrid and playerTargetGrid
        #if wrong, write O on computerPrimaryGrid and playerTargetGrid
        #if 
        

os.system('cls')
createMap(userPrimaryGrid)
createMap(userTargetGrid)
createMap(computerPrimaryGrid)
createRandomGrid(computerPrimaryGrid)
printScreen(computerPrimaryGrid, computerTargetGrid)
input(" stop")
printScreen(userPrimaryGrid, userTargetGrid)
placeShips(userPrimaryGrid)
#print(userMap)
