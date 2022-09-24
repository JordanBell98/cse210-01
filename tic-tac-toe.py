'''
Tic-Tac-Toe Game
Author: Jordan Bell
''' 

def main():
    print("Welcome to Tic-Tac-Toe!")
    player = next_player("")
    board = create_board()

    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)

    loser = player
    winner = next_player(player)


    if is_a_draw(board) == True:
        print("Aww looks like you ended in a draw, you two are both really good!")
    else:
        print(f"Congratulations {winner}'s you won the game!")
        print(f"Better luck next time {loser}'s")
    print("Thanks for playing!")

    play_again = input("Would you like to play again (Y/N)?  ")
    '''Added some new end game statements and a request to play again'''

    if play_again == "Y" or play_again == "y":
        main()
    else:
        print("Ok, until next time then!")

    ''' My attempt I couldn't quite figure it out
        while game_condition != 1 and game_condition !=2:
        Make Move
        
        is_a_draw(board)
        has_winner(board)
        if game_condition == 1:
        Player {} wins the game
        if game_condition == 2:
        Draw condition'''


def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board


def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-----')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-----')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()    

def is_a_draw(board):
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
        if has_winner(board):
            return False      
    return True 
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"


if __name__ == "__main__":
    main()