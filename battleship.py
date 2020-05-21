import os

userMap = [['.' for x in range(11)] for y in range(11)]
computerMap = [['.' for x in range(10)] for y in range(10)]
shipLengths = [["Carrier", 5], ["Battleship", 4], ["Cruiser", 3], ["Submarine", 3], ["Destroyer", 2]]

def createMap(map):
	map[0][0] = " "
	letter = 64
	for x in range(1, 11):
		map[0][x] = chr(letter + x)
	for y in range(1, 11):
		map[y][0] = y
	

def printScreen(map):
	#os.system('cls')
	for x in range(11):
		if x == 0:
			print("    ", end='')
		else:
			print(str("{:02d}".format(map[x][0])) + "  ", end='')
		for y in range(1, 11):
			print(str(map[x][y]) + " ", end='')
		print("")
		
def placeShips(map):
	for ship in shipLengths:
		shipHead = input("Where would you like to place the " + ship[0] + " (" + str(ship[1]) + " spaces)?  Use the format LETTERNUMBER (e.g. B5): ")
		shipHeadParsed = [ord(shipHead.upper()[:1]) - 64, int(shipHead[1:])]
		print(shipHeadParsed)
		#horizontally or vertically?
		dir = input("Enter Down to place ship down from ship head, or Right to place the ship to the right:")
		print(dir)
		if dir.lower() == "down":
			print(dir)
			if 0 < shipHeadParsed[0] < 11 and 0 < shipHeadParsed[1] < 11 and 0 < shipHeadParsed[0] + ship[1] < 11:
				print("iN")
				i = 0
				while(i < ship[1]):
					map[shipHeadParsed[0]+i][shipHeadParsed[1]] = u"\u25A0"
					i += 1
		#if shiphead and tail are in bound, write them as squares
		if dir.lower() == "right":
			if 0 < shipHeadParsed[0] < 11 & 0 < shipHeadParsed[1] < 11 & 0 < shipHeadParsed[1] + ship[1] < 11:
				i = 0
				while(i < ship[1]):
					map[shipHeadParsed[0]][shipHeadParsed[1]+i] = u"\u25A0"
					i += 1
		printScreen(map)
		
os.system('cls')
createMap(userMap)
printScreen(userMap)
placeShips(userMap)
#print(userMap)