import os

userMap = [['.' for x in range(11)] for y in range(11)]
computerMap = [['.' for x in range(10)] for y in range(10)]
ships = [["Carrier", 5], ["Battleship", 4], ["Cruiser", 3], ["Submarine", 3], ["Destroyer", 2]]

def createMap(map):
	#blank top left
	map[0][0] = "  "
	#ascii base letter
	letter = 64
	#create alpha column header
	for col in range(1, 11):
		map[0][col] = chr(letter + col)
	#create numeric row header
	for row in range(1, 11):
		map[row][0] = "{:02d}".format(row)
	

def printScreen(map):
	#os.system('cls')
	'''for x in range(11):
		if x == 0:
			print("    ", end='')
		else:
			print(str("{:02d}".format(map[x][0])) + "  ", end='')
		for y in range(1, 11):
			print(str(map[y][x]) + " ", end='')
		print("")'''
	for row in map:
		for value in row:
			print(str(value) + " ", end='')
		print('')
		
def placeShips(map):
	for ship in ships:
		while True:
			name, length = ship[0], ship[1]
			#prompt for ship's coordinates
			head = input("Where would you like to place the " + name + " (" + str(length) + " spaces)?  Use the format LETTERNUMBER (e.g. B5): ")
			#assign to x and y coords
			col, row = ord(head.upper()[:1]) - 64, int(head[1:])
			print("col=" + str(col))
			#get ship direction
			dir = input("Down or Right: ").lower()
			if 0 < col < 11 and 0 < row < 11 and 0 < col + length < 11 and shipOnFreeSpace(col, row, length, map, dir):
				break
			else:
				print("Invalid coordinates, please try again")
		i = 0
		print("col= " + str(col) + " row= " + str(row))
		if dir == "down":
			while(i < length):
				map[row + i][col] = u"\u25A0"
				i += 1
		if dir == "right":
			while(i < length):
				map[row][col + i] = u"\u25A0"
				i += 1
		printScreen(map)
					

def shipOnFreeSpace(col, row, len, map, dir):
	i = 0
	if dir == "down":
		while i < len:
			if map[row][col + i] != '.':
				return False
			i += 1
	elif dir == "right":
		while i < len:
			if map[row + i][col] != '.':
				return False;
			i += 1			
	return True
		
os.system('cls')
createMap(userMap)
printScreen(userMap)
placeShips(userMap)
#print(userMap)
