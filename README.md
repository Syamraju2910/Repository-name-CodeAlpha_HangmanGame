# CodeAlpha Hangman Game

## Objective
Create a simple text-based Hangman game where the player guesses a word one letter at a time.

## CodeAlpha Requirements
- Use a small list of 5 predefined words.
- Limit incorrect guesses to 6.
- Use basic console input/output.
- Use Python concepts such as `random`, loops, conditions, strings, and lists.

## Features
- Randomly selects one of five predefined words.
- Accepts one letter at a time.
- Prevents duplicate guesses.
- Tracks incorrect guesses.
- Displays remaining attempts.
- Shows the word when the player wins or loses.

## Technologies
- Python 3
- Standard library only

## How to Run
1. Install Python 3.
2. Open a terminal in this folder.
3. Run:
   `python hangman.py`

## Sample Output
```text
=== CodeAlpha Hangman Game ===
Guess the hidden word one letter at a time.
You have 6 incorrect guesses.

Word: _ _ _ _ _ _
Enter a letter: p
Correct guess!

Word: p _ _ _ _ _
Enter a letter: y
Correct guess!

...
Congratulations! You guessed the word: python
```

## Project Structure
```text
CodeAlpha_HangmanGame/
├── hangman.py
├── README.md
└── screenshots/
```
