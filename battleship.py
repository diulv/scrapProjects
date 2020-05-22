import os

userMap = [['.' for x in range(11)] for y in range(11)]
computerMap = [['.' for x in range(10)] for y in range(10)]
ships = [["Carrier", 5], ["Battleship", 4], ["Cruiser", 3], ["Submarine", 3], ["Destroyer", 2]]

def createMap(map):
	map[0][0] = " "
	letter = 64
	for x in range(1, 11):
		map[0][x] = chr(letter + x)
	for y in range(1, 11):
		map[y][0] = y
	

def printScreen(map):
	os.system('cls')
	for x in range(11):
		if x == 0:
			print("    ", end='')
		else:
			print(str("{:02d}".format(map[x][0])) + "  ", end='')
		for y in range(1, 11):
			print(str(map[x][y]) + " ", end='')
		print("")
		
def placeShips(map):
	for ship in ships:
		while True:
			name, length = ship[0], ship[1]
			head = input("Where would you like to place the " + name + " (" + str(length) + " spaces)?  Use the format LETTERNUMBER (e.g. B5): ")
			xCoord, yCoord = ord(head.upper()[:1]) - 64, int(head[1:])
			dir = input("Down or Right: ").lower()
			if dir == "down" and 0 < xCoord < 11 and 0 < yCoord < 11 and 0 < xCoord + length < 11 and shipOnFreeSpace(xCoord, yCoord, xCoord + length, yCoord, map, dir):
				break
			elif dir.lower() == "right" and 0 < xCoord < 11 and 0 < yCoord < 11 and 0 < yCoord + length < 11 and shipOnFreeSpace(xCoord, yCoord, xCoord, yCoord + length, map, dir):
				break
			else:
				print("Invalid coordinates, please try again")
		i = 0
		if dir == "down":
			while(i < length):
				map[xCoord + i][yCoord] = u"\u25A0"
				i += 1
		if dir == "right":
			while(i < length):
					map[xCoord][yCoord + i] = u"\u25A0"
					i += 1
		printScreen(map)
					

def shipOnFreeSpace(xHead, yHead, xTail, yTail, map, dir):
	if dir == "right":
		i = yHead
		while i <= yTail:
			if map[xHead][i] != '.':
				return False;
			i += 1
	
	elif dir == "down":
		i = xHead
		while i <= xTail:
			if map[i][yHead] != '.':
				return False
			i += 1
	return True
		
os.system('cls')
createMap(userMap)
printScreen(userMap)
placeShips(userMap)
#print(userMap)
