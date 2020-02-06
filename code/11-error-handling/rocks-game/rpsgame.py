import datetime
import random
import json
import os

from colorama import Fore

rolls = {}


def main():
    try:
        print(Fore.WHITE)
        log("App starting up...")

        show_header()
        load_rolls()
        show_leaderboard()

        player1, player2 = get_players()
        log(f"{player1} has logged in.")

        play_game(player1, player2)
        log("Game over.")
    except json.decoder.JSONDecodeError as je:
        print()
        print(Fore.LIGHTRED_EX + "ERROR: The file rolls.json is invalid JSON." + Fore.WHITE)
        print(Fore.LIGHTRED_EX + f"ERROR: {je}" + Fore.WHITE)
    except FileNotFoundError as fe:
        print()
        print(Fore.LIGHTRED_EX + "ERROR: Rolls file not found" + Fore.WHITE)
        print(Fore.LIGHTRED_EX + f"ERROR: {fe}" + Fore.WHITE)
    except KeyboardInterrupt:
        print()
        print(Fore.LIGHTCYAN_EX + "You gotta run? Ok, cya next time!" + Fore.WHITE)
    except Exception as x:
        print(Fore.LIGHTRED_EX + f"Unknown error: {x}" + Fore.WHITE)


def show_header():
    print(Fore.LIGHTMAGENTA_EX)
    print("---------------------------")
    print("    Rock Paper Scissors")
    print("   Error Handling Edition")
    print("---------------------------")
    print(Fore.WHITE)


def show_leaderboard():
    leaders = load_leaders()

    sorted_leaders = list(leaders.items())
    sorted_leaders.sort(key=lambda l: l[1], reverse=True)

    print()
    print("---------------------------")
    print("LEADERS:")
    for name, wins in sorted_leaders[0:5]:
        print(f"{wins:,} -- {name}")
    print("---------------------------")
    print()


def get_players():
    p1 = input("Player 1, what is your name? ")
    p2 = "Computer"

    return p1, p2


def play_game(player_1, player_2):
    log(Fore.CYAN + f"New game starting between {player_1} and {player_2}.")

    wins = {player_1: 0, player_2: 0}
    roll_names = list(rolls.keys())

    while not find_winner(wins, wins.keys()):
        roll1 = get_roll(player_1, roll_names)
        roll2 = random.choice(roll_names)

        if not roll1:
            print(Fore.LIGHTRED_EX + "Try again!")
            print(Fore.WHITE)
            continue

        log(f"Round: {player_1} roll {roll1} and {player_2} rolls {roll2}")
        print(Fore.YELLOW + f"{player_1} rolls {roll1}")
        print(Fore.LIGHTBLUE_EX + f"{player_2} rolls {roll2}")
        print(Fore.WHITE)

        winner = check_for_winning_throw(player_1, player_2, roll1, roll2)

        if winner is None:
            msg = "This round was a tie!"
            print(msg)
            log(msg)
        else:
            msg = f'{winner} takes the round!'
            fore = Fore.GREEN if winner == player_1 else Fore.LIGHTRED_EX
            print(fore + msg + Fore.WHITE)
            log(msg)
            wins[winner] += 1

        msg = f"Score is {player_1}: {wins[player_1]} and {player_2}: {wins[player_2]}."
        print(msg)
        log(msg)
        print()

    overall_winner = find_winner(wins, wins.keys())
    fore = Fore.GREEN if overall_winner == player_1 else Fore.LIGHTRED_EX
    msg = f"{overall_winner} wins the game!"
    print(fore + msg + Fore.WHITE)
    log(msg)
    record_win(overall_winner)


def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name, 0) >= best_of:
            return name

    return None


def check_for_winning_throw(player_1, player_2, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print("The play was tied!")

    outcome = rolls.get(roll1, {})
    if roll2 in outcome.get('defeats'):
        return player_1
    elif roll2 in outcome.get('defeated_by'):
        return player_2

    return winner


def get_roll(player_name, roll_names):
    try:
        print("Available rolls:")
        for index, r in enumerate(roll_names, start=1):
            print(f"{index}. {r}")

        text = input(f"{player_name}, what is your roll? ")
        if text is None or not text.strip():
            print("You must enter response")
            return None

        selected_index = int(text) - 1

        if selected_index < 0 or selected_index >= len(roll_names):
            print(f"Sorry {player_name}, {text} is out of bounds!")
            return None

        return roll_names[selected_index]
    except ValueError as ve:
        print(Fore.RED + f"Could not convert to integer: {ve}" + Fore.WHITE)
        return None


def load_rolls():
    global rolls

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'rolls.json')

    with open(filename, 'r', encoding='utf-8') as fin:
        rolls = json.load(fin)

    log(f"Loaded rolls: {list(rolls.keys())} from {os.path.basename(filename)}.")


def load_leaders():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'leaderboard.json')

    if not os.path.exists(filename):
        return {}

    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)


def record_win(winner_name):
    leaders = load_leaders()

    if winner_name in leaders:
        leaders[winner_name] += 1
    else:
        leaders[winner_name] = 1

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'leaderboard.json')

    with open(filename, 'w', encoding='utf-8') as fout:
        json.dump(leaders, fout)


def log(msg):
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'rps.log')

    with open(filename, 'a', encoding='utf-8') as fout:
        fout.write(f"[{datetime.datetime.now().date().isoformat()}] ")
        fout.write(msg)
        fout.write('\n')


if __name__ == '__main__':
    main()
