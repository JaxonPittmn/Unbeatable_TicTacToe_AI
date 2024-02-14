import os
#Global Variables
board = []
row = 0
col = 0
count = 0
player = ""
winner_found = False
#Checks every spot
def minimax(player):
    #Base case here
    if check_win("X"):
        return (-10, None, None)
    elif check_win("O"):
        return (10, None, None)
    elif check_tie():
        return (0, None, None)
    
    #Recursion here
    optimalRow = -1
    optimalCol = -1
    if player == "X":
        worst = 1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    place_player("X", row, col)
                    moveVal = minimax("O")[0]
                    if moveVal < worst:
                        worst = moveVal
                        optimalRow = row
                        optimalCol = col
                    place_player("-", row, col)
        return(worst, optimalRow, optimalCol)
    else:
        best = -1000
        for row in range(3):
            for col in range(3):
                 if board[row][col] == "-":
                    place_player("O", row, col)
                    moveVal = minimax("X")[0]
                    if moveVal > best:
                        best = moveVal
                        optimalRow = row
                        optimalCol = col
                    place_player("-", row, col)
    return (best, optimalRow, optimalCol)
for i in range(3):
    board.append(["-", "-", "-"])
def print_board():
    print("\t0\t\t1\t\t2")
    count = 0
    for i in board:
        row = ""
        for space in i:
            row += "\t" + space + "\t"
        print(count, row + "\n")
        count += 1

#returns true if a row,col on the board is open
def is_valid_move(row, col):
    if board[row][col] == "X" or board[row][col] == "O":
        print("Please enter a valid move")
        return False
    if row > 2 or row < 0 or col > 2 or col < 0:
        print("Please enter a valid move")
        return False
    else:
        return True
def is_valid_move_npc(row, col):
    if board[row][col] == "X" or board[row][col] == "O":
        return False
    if row > 2 or row < 0 or col > 2 or col < 0:
        return False
    else:
        return True
#places player on row,col on the board
def place_player(player, row, col):
    board[row][col] = player
    
#Adds user location to the board, and prints the board
def take_turn(player, row, col):
    player = "X"
    print(player + "'s Turn")
    is_valid_move_bool = False
    while not is_valid_move_bool:
        row = int(input("Enter a row "))
        col = int(input("Enter a col "))
        is_valid_move_bool = is_valid_move(row, col)
    if is_valid_move(row, col):
        place_player(player, row, col)
#Npc turn
def npc_turn(player, row, col):
    player = "O"
    print(player + "'s Turn")
    is_valid_move_bool = False
    while not is_valid_move_bool:
        row = minimax(player)[1]
        col = minimax(player)[2]
        is_valid_move_bool = is_valid_move_npc(row, col)
    if is_valid_move(row, col):
        place_player(player, row, col)

#Check win functions here:
def check_win(player):
    return check_row_win(player) or check_col_win(player) or check_diag_win(player)
def check_tie():
    for x in board:
        if "-" in x:
            return False
    return True
   
def check_row_win(player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    return False
def check_col_win(player):
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    return False
def check_diag_win(player):
    if board[0][0] == player and board [1][1] == player and board[2][2] == player:
        return True
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    else:
        return False
#Start of program
print("\t\tWelcome to Tic Tac Toe!")
while not winner_found and not check_tie():
    if count % 2 == 0:
        print_board()
        take_turn(player, row, col)
        os.system('clear')
        if check_win("X"):
            winner_found = True
            player = "X"
    else:
        print_board()
        npc_turn(player, row, col)
        os.system('clear')
        if check_win("O"):
            winner_found = True
            player = "O"
    count += 1
if check_tie():
    print_board()
    print("Tie")
if winner_found:
    print_board()
    print(f"The winner is {player}!")