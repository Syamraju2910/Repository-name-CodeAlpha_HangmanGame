import random

WORDS = ["python", "coding", "programming", "computer", "developer"]
MAX_WRONG_GUESSES = 6


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("\n=== CodeAlpha Hangman Game ===")
    print("Guess the hidden word one letter at a time.")
    print(f"You have {MAX_WRONG_GUESSES} incorrect guesses.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        display = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in word
        )
        print("Word:", display)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            return

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!\n")
        else:
            wrong_guesses += 1
            print(
                f"Wrong guess! Remaining attempts: "
                f"{MAX_WRONG_GUESSES - wrong_guesses}\n"
            )

    print("Game over! The word was:", word)


if __name__ == "__main__":
    play_hangman()
