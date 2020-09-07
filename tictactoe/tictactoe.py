board = [[' ' for x in range(3)] for y in range(3)]

def printBoard(board):
    print("  A B C")
    print(" +-----+")
    for idx, row in enumerate(board):
        print(str(idx + 1), end='')
        for val in row:
            print("|" + str(val), end='')
        print("|")
        if idx == 2:
            print(" +-----+")
        else:
            print(" |-----|")
            

    
def placePiece():
    placement = input("Where would you like to place a piece?  Enter in LETTERNUMBER, e.g. A2: ")
    row = int(ord(placement[:1]) - 64) - 1
    column = int(placement[1:]) - 1
    board[column][row] = 'X'
    printBoard(board)
    
def checkWinner(playerChar):
    winningArray = [playerChar, playerChar, playerChar]
    for i in range(3):
        if board[i] == winningArray:
            return True
        if [board[0][i], board[1][i], board[2][i]] == winningArray:
            return True
    if [board[0][0], board[1][1], board[2][2]] == winningArray:
        return True
    
    
printBoard(board)
placePiece()
checkWinner('X')
