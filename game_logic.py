import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects and returns a random word from the WORDS list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the current state of the game, including the snowman stage,
    the secret word with guessed letters revealed, and previously
    guessed letters.

    Args:
        mistakes (int): The number of incorrect guesses made so far.
        secret_word (str): The word the user is trying to guess.
        guessed_letters (list): A list of the letters guessed so far.
    """
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print("\n")


def play_game():
    """
    Initializes and manages a single round of the Snowman game,
    including selecting a secret word, handling user input, and
    determining win/loss conditions.
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while True:  # Loop until break
        display_game_state(mistakes, secret_word, guessed_letters)

        # Get user input
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already tried that letter.")
            continue

        guessed_letters.append(guess)

        # Check the guess
        if guess in secret_word:
            print("Good guess!")
            # Check for win
            won = True
            for letter in secret_word:
                if letter not in guessed_letters:
                    won = False
                    break
            if won:
                print(
                    f"\nCongratulations! You guessed the word: {secret_word}")
                display_game_state(mistakes, secret_word, guessed_letters)
                break  # Exit loop
        else:
            print("Incorrect guess!")
            mistakes += 1
            # Check for loss
            if mistakes >= len(STAGES) - 1:
                display_game_state(mistakes, secret_word, guessed_letters)
                print(
                    f"\nGame Over! The snowman melted. The word was: {secret_word}"
                )
                break  # Exit loop
