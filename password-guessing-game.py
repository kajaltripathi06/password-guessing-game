import random

easy_words = ["apple", "train", "tiger", "cat", "pen", "toy", "mouse"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop", "mobile", "google"]
hard_words = ["butterfly", "elephant", "umbrella", "router", "mountain", "bouquet", "speaker"]

MAX_ATTEMPTS = 5


def choose_secret(level):
    """Pick a random word based on the chosen difficulty level."""
    if level == "easy":
        return random.choice(easy_words)
    elif level == "medium":
        return random.choice(medium_words)
    elif level == "hard":
        return random.choice(hard_words)
    else:
        print("Invalid choice. Defaulting to easy level")
        return random.choice(easy_words)


def get_hint(guess, secret):
    """Build a hint string showing which letters are in the correct position."""
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
    return hint


def play_round():
    """Play a single round of the guessing game."""
    level = input("Enter Difficulty level: ").lower()
    secret = choose_secret(level)

    attempts = 0
    print("\nGuess the password")

    while attempts < MAX_ATTEMPTS:
        guess = input("Enter your guess = ").lower()
        attempts += 1

        if guess == secret:
            print(f'Congratulations you guessed the password in {attempts} attempts.')
            break

        hint = get_hint(guess, secret)
        print("Hint: ", hint)

        if attempts == MAX_ATTEMPTS:
            print("\nyour attempts are over.")
            print(f'correct password is : {secret}')
        else:
            print(f'attempts left: {MAX_ATTEMPTS - attempts}')

    print("GAME OVER")


def main():
    print("Welcome to the password guessing game")
    print("Choose the difficulty level: easy , medium or hard")

    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
