board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_", ]

currentplayer = "X"
gameisgoing=True
winner=None
count=0
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
def handle_turns():
    position=int(input("Enter the position number:"))
    board[position]=currentplayer

def swap_players():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    elif currentplayer== "O":
        currentplayer= "X"
def check_who_is_winner():

    global winner
    rowwinner = check_row()
    colwinner = check_column()
    diawinner = check_dia()

    if rowwinner:
        winner = rowwinner
    elif colwinner:
        winner = colwinner
    elif diawinner:
        winner = diawinner



def check_row():
    global gameisgoing
    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"
    if row1 or row2 or row3:
        gameisgoing = False
    if row1:
        return board[2]
    if row2:
        return board[5]
    elif row3:
        return board[7]
def check_column():
    global gameisgoing
    col1 = board[0] == board[3] == board[6] != "_"
    col2 = board[1] == board[4] == board[7] != "_"
    col3 = board[2] == board[5] == board[8] != "_"
    if col1 or col2 or col3:
        gameisgoing = False
    if col1:
        return board[3]
    if col2:
        return board[7]
    elif col3:
        return board[8]
def check_dia():
    global gameisgoing
    dai1 = board[0] == board[4] == board[8] != "_"
    dai2 = board[2] == board[4] == board[6] != "_"

    if dai1 or dai2:
        gameisgoing = False
    if dai1:
        return board[4]
    elif dai2:
        return board[6]



def play_game():
    global gameisgoing
    while gameisgoing:
        display_board()
        handle_turns()
        swap_players()
        check_who_is_winner()



    if winner=="X":
        print("X is winner")
    elif winner=="O":
        print("O is winner")
    elif winner=="None":
            print("Game Drawn")
            print("\n")




play_game()





