#Global Variables
#making board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_is_still_going = True

#who won?
winner = None
current_player = 'x'

#display board
def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

def play_game():
    #display initial board
    display_board()
    
    while game_is_still_going:

        #handles the turn to the arbitary player        
        handle_turn(current_player)
        
        #check if the game is over
        check_if_game_over()

        #flip from the other player
        flip_player()

    #if game is over
    if winner == 'x' or winner == 'o':
        print(winner+" Won.")
    elif winner == None:
        print("Tie.")
#input from the user
def handle_turn(player):

    print(player + " 's turn")
    position = input("Enter a position from 1-9: ")
    #checking for the overriten input from the user
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
             position = input("Enter a position from 1-9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there.Go again.")

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    #set up global variable
    global winner
    
    #check row
    row_winner = check_rows()
    #check colomn
    column_winner = check_columns()
    #check diagonal
    diagonal_winner = check_diagonals()

    #get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():

    #set up global variable
    global game_is_still_going
    #check if any row has same value
    row_1 = board[0]==board[1] == board[2] != '-'
    row_2 = board[3]==board[4] == board[5] != '-'
    row_3 = board[6]==board[7] == board[8] != '-'
    #if any row get match , flag taht ihere is win
    if row_1 or row_2 or row_3:
        game_is_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    #set up global variable
    global game_is_still_going

    #check if any column has same value
    column_1 = board[0]==board[3] == board[6] != '-'
    column_2 = board[1]==board[4] == board[7] != '-'
    column_3 = board[2]==board[5] == board[8] != '-'

    #if any column get match , flag taht ihere is win
    if column_1 or column_2 or column_3:
        game_is_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    #set up global variable
    global game_is_still_going

    #check if any diagonals has same value
    diagonals_1 = board[0]==board[4] == board[8] != '-'
    diagonals_2 = board[6]==board[4] == board[2] != '-'
    

    #if any diagonals get match , flag taht ihere is win
    if diagonals_1 or diagonals_2 :
        game_is_still_going = False

    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    
    return

def check_if_tie():
    global game_is_still_going
    if "-" not in board:
        game_is_still_going = False
    return

def flip_player():
    # set a global variable
    global current_player
    #if current_player is "x" then flip to "0"
    if current_player =="x":
        current_player = "0"
    #if current_player is "o" then flip to "x"
    elif current_player == "0":
        current_player = "x"
        
    return


play_game()










#make board
#disply board
#play game
#handle turn
#check win
    #check row
    #check colomn
    #check diagonal
#check tie
#flip player
