import numpy as np

def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0

def checkWin(board):
    #transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
end = False
pieces = {0:"X", 1:"0"}
turn = 0
while end == False:
    move = -1
    while not(-1 < int(move) and int(move) < 9):
        try:
            move = input("Please enter a the square you want to use (eg, 0 - 8)")
            move = int(move)
        except ValueError:
            move = -1
    if board[int(move) // 3][int(move) % 3] == " ":
        board[int(move) // 3][int(move) % 3] = pieces[turn % 2]
        print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}\n ----\n{board[1][0]}|{board[1][1]}|{board[1][2]}\n ----\n{board[2][0]}|{board[2][1]}|{board[2][2]}\n")
        res = checkWin(board)
        if res != 0 and res != " ":
            print(f"The winner is {res}")
            end == True
            break
        turn += 1