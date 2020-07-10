import random


def main():
    show_header()
    play_game()


def show_header():
    print("------------------------------")
    print("     M&M guessing game!")
    print("------------------------------")

    print("Guess the number of M&Ms and you get lunch on the house!")
    print()


def get_guess_from_user():
    guess_text = input("How many M&Ms are in the jar? ")
    guess = int(guess_text)
    return guess


def evaluate_guess(guess, actual_count):
    if actual_count == guess:
        print(f"You got a free lunch! It was {guess}.")
    elif guess < actual_count:
        print("Sorry, that's too LOW!")
    else:
        print("That's too HIGH!")

    return actual_count == guess


def play_game():
    mm_count = random.randint(1, 100)
    attempt_limit = 5
    attempts = 0

    while attempts < attempt_limit:
        guess = get_guess_from_user()
        attempts += 1

        won = evaluate_guess(guess, mm_count)
        if won:
            break

    print(f"Bye, you're done in {attempts} attempts!")


if __name__ == '__main__':
    main()
