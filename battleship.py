import os

userMap = [['.' for x in range(11)] for y in range(11)]
computerMap = [['.' for x in range(11)] for y in range(11)]
SHIPS = [["Carrier", 5], ["Battleship", 4], ["Cruiser", 3], ["Submarine", 3], ["Destroyer", 2]]

def createMap(map):
	#blank top left
	map[0][0] = "  "
	#create alpha column header
	letter = 64
	for col in range(1, 11):
		map[0][col] = chr(letter + col)
	#create numeric row header
	for row in range(1, 11):
		map[row][0] = "{:02d}".format(row)
	

def printScreen(map):
	for row in map:
		for value in row:
			print(str(value) + " ", end='')
		print('')
		
def placeShips(map):
	for ship in SHIPS:
		while True:
			name, length = ship[0], ship[1]
			#prompt for ship's coordinates
			shipHead = input("Where would you like to place the " + name + " (" + str(length) + " spaces)?  Use the format LETTERNUMBER (e.g. B5): ")
			#assign to x and y coords
			col = ord(shipHead.upper()[:1]) - 64
			row = int(shipHead[1:])
			#get ship direction
			print("col= " + str(col) + " row= " + str(row))
			dir = input("Down or Right: ").lower()
			if shipOnFreeSpace(col, row, length, map, dir):
				break
			else:
				print("Invalid coordinates, please try again")
        placeShip(col, row, length, map, dir)
		'''
		i = 0
		if dir == "down":
			while(i < length):
				map[row + i][col] = u"\u25A0"
				i += 1
		if dir == "right":
			while(i < length):
				map[row][col + i] = u"\u25A0"
				i += 1
        '''
		printScreen(map)
					
#if each space we place a ship is not free or valid, return false
def shipOnFreeSpace(col, row, len, map, dir):
    print("in")
    if dir == "down":
        print("2")
        try:
            for i in range(len):
                print(' row= ' + str(row + i) + 'col= ' + str(col) + ' space= ' + str(map[row+i][col]))
                if map[row + i][col] != '.':
                    return False
        except:
            return False
    elif dir == "right":
        try:
            for i in range(len):
                print(' row= ' + str(row) + 'col= ' + str(col+i) + ' space= ' + str(map[row][col+i]))
                if map[row][col + i] != '.':
                    return False
        except:
            return False
    return True

def placeShip(col, row, len, map, dir):
    if dir == "down":
        for i in range(len):
            map[row + i][col] = u"\u25A0"
    elif dir == "right":
        for i in range(len)
            map[row][col + i] = u"\u25A0"

def createRandomBoard():
    return 0
		
os.system('cls')
createMap(userMap)
printScreen(userMap)
placeShips(userMap)
#print(userMap)
