# √ choose the players
# √ create the board
# √ choose an initial player
# √ until someone wins, check for winner
#    show the board
#    choose location, mark it
#    toggle active player

# game over, active player won!


def main():
    # CREATE THE BOARD:
    # Board is a list of rows
    # Rows are a list of cells
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

    # CHOOSE INITIAL PLAYER
    active_player_index = 0
    players = ["You", "Computer"]
    symbols = ["X", "O"]

    # UNTIL SOMEONE WINS
    while not find_winner(board):
        print("Play a round...")


def find_winner(board):
    # TODO: Implement how we check for a winner!
    return False


if __name__ == '__main__':
    main()
