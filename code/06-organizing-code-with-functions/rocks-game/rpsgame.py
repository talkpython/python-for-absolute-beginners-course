import random


def main():
    show_header()
    play_game("You", "Computer")


def show_header():
    print("---------------------------")
    print(" Rock Paper Scissors v1")
    print("---------------------------")


def play_game(player_1, player_2):
    rolls = ['rock', 'paper', 'scissors']

    roll1 = get_roll(player_1, rolls)
    roll2 = random.choice(rolls)

    if not roll1:
        print("Can't play that, exiting")
        return

    print(f"{player_1} roll {roll1}")
    print(f"{player_2} rolls {roll2}")

    winner = check_for_winning_throw(player_1, player_2, roll1, roll2)

    print("The game is over!")
    if winner is None:
        print("It was a tie!")
    else:
        print(f'{winner} takes the game!')


def check_for_winning_throw(player_1, player_2, roll1, roll2):
    # Rock
    #     Rock -> tie
    #     Paper -> lose
    #     Scissors -> win
    # Paper
    #     Rock -> win
    #     Paper -> tie
    #     Scissors -> lose
    # Scissors
    #     Rock -> lose
    #     Paper -> win
    #     Scissors -> tie
    winner = None
    if roll1 == roll2:
        print("The play was tied!")
    elif roll1 == 'rock':
        if roll2 == 'paper':
            winner = player_2
        elif roll2 == 'scissors':
            winner = player_1
    elif roll1 == 'paper':
        if roll2 == 'scissors':
            winner = player_2
        elif roll2 == 'rock':
            winner = player_1
    elif roll1 == 'scissors':
        if roll2 == 'rock':
            winner = player_2
        elif roll2 == 'paper':
            winner = player_1
    return winner


def get_roll(player_name, rolls):
    roll = input(f"{player_name}, what is your roll? [rock, paper, scissors]: ")
    roll = roll.lower().strip()
    if roll not in rolls:
        print(f"Sorry {player_name}, {roll} is not a valid play!")
        return None

    return roll


if __name__ == '__main__':
    main()
