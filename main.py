import random
def display_board(board):
    blankBoard="""
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""
    for i in range(1,10):
        if board[i] == 'O' or board[i] == 'X':
            blankBoard = blankBoard.replace(str(i),board[i])
        else:
            blankBoard = blankBoard.replace(str(i),' ')
    print(blankBoard)

def player_input():
    while True:
        player1 = input("choose your marker X or O? ").upper()
        if player1 == 'X':
            player2 = 'O'
            print(f"you've chose {player1}, the computer will be {player2}\n")
            return player1,player2
        elif player1 == 'O':
            player2 = 'X'
            print(f"you've chose {player1}, the computer will be {player2}\n")
            return player1,player2

def place_marker(board , marker, position):
    board[position] = marker
    return board

def is_empty(board,position):
    return board[position] == '#'

def player_choice(board):
    print("your turn: ")
    choice = input("select an empty place between 1 and 9: ")
    while not is_empty(board,int(choice)):
        choice = input("this space isn't free, select a place between 1 and 9: ")
    return int(choice)

def computer_choice(board):
    print("computer's turn:")
    choice = random.randint(1,9)
    while not is_empty(board,choice):
        choice = random.randint(1,9)
    return choice
def fullboard_check(board):
    return len([x for x in board if x == '#']) == 1
    # for i in range(1,10):
    #     if board[i] == '#':
    #         return False
    #     return True

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False

def play_again():
    while True:
        response = input("press ENTER if you want to play again,"
                         " otherwise will exit the game")
        if not response:
            return True
        return False

if __name__ == "__main__":
    while True:
        print("""
____________________________________
|    welcome to Tic Tac Toe game    | 
|___________________________________|
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
""")
        board = ['#','#','#','#','#','#','#','#','#','#']
        i = 1
        player1_marker,computer_marker = player_input()
        while not fullboard_check(board):
            if i % 2 == 0:
                marker = computer_marker
                position = computer_choice(board)

            else:
                marker = player1_marker
                position = player_choice(board)

            place_marker(board,marker,position)
            i+=1
            display_board(board)
            if win_check(board,marker):
                print(f"$$$$ {marker} won the game $$$$")
                break
        if not play_again():
            break
