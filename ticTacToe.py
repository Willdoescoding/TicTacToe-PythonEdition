# Tic-Tac-Toe Game
# X always go first, then O next. Player will be asked to choose to go first or the computer goes first.
# Variables for X and Os, square numbers, EMPTY slot, and Tie
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

# functions
# display the board on console/ terminal
def display_instruct():
    '''

     0 | 1 | 2
   -------------
     3 | 4 | 5
   -------------
     6 | 7 | 8

    '''

def ask_yes_no(qs):
    response = None
    while response not in ("y", "n"):
        response = input(qs).lower()
    return response

def ask_no(qs, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(qs))
    return response

def pieces():
    go_first = ask_yes_no("Do you require to go first? (y/n):")
    if go_first == "y":
        print("\nYou first")
        human = X
        computer = O
    else:
        print("Your computer goes first")
        computer = X
        human = O
    return computer, human

def new_board():
    board = []

    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print("\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------" )
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    WAYS_TO_WIN =(

        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    )

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

def human_move(board, human):
    legal = legal_moves(board)
    move = None

    while move not in legal:
        move = ask_no("Where will you move? (0-8): ", 0, NUM_SQUARES)

        if move not in legal:
            print("\nThat square is occupied. Try Again")

    return move

def computer_move(board, computer, human):
    board = board[:]

    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("My turn:", end=" ")

    for move in legal_moves(board):
        board[move] = computer

        if winner (board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human

        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    if turn == "X":
        return O
    else:
        return X

def congrats_winner(the_winner, computer, human):
    if the_winner != TIE:
        print("Hard Luck!")
    else:
        print("TIE")

    if the_winner == computer:
        print("Computer Won!")
    else:
        print("Well Done")

# main 
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer

        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrats_winner(the_winner, computer, human)

main()
input("\nPress ENTER To Quit The Game")


