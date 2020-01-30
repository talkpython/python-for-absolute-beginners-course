# create the board
# choose an initial player
# until someone wins, check for winner
#    show the board
#    choose location, mark it
#    toggle active player

# game over, active player won!


def main():
    # Board is a list of rows
    # Rows are a list of cells
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
    # board.get("1,2")
    # board[2]

    # board=  {
    #     "0,0": None,
    #     "0,1": None,
    #     "0,2": None,
    #     "1,0": None,
    #     "1,2": None,
    # }

    # board = [
    #     [cell1, cell2, cell3],
    #     [r2_c1, r2_c2, r2_c3],
    #     [r3_c1, r3_c2, r3_c3]
    # ]

    # board = [
    #     [X, X, 0],
    #     [X, _, 0],
    #     [X, 0, _]
    # ]
    # r2_c3= board[1][2]


if __name__ == '__main__':
    main()
