# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a console-based Hangman game to practice string manipulation, loops, conditionals, and user input handling. Implement the core game loop, input validation, and win/lose logic.

## 📝 Tasks

### 🛠️	Core Hangman Implementation

#### Description
Implement the main Hangman gameplay: randomly choose a word, accept letter guesses from the player, reveal correct letters in the word, and track remaining incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list of at least 10 words.
- Display the current progress of the word using underscores and spaces (e.g., _ _ a _ _).
- Accept single-letter guesses (case-insensitive) and update the display for correct guesses.
- Track and decrement the number of remaining incorrect attempts (suggested default: 6).
- Prevent repeated guesses from counting against the player; show a message for repeated guesses.
- End the game when the word is fully guessed (win) or when attempts reach zero (loss), and display a clear win/lose message including the secret word.

Example interaction:

```
Secret word: _ _ _ _ _
Guess a letter: a
Good guess! _ a _ _ _
Incorrect guesses remaining: 6
Guess a letter: z
Nope. Incorrect guesses remaining: 5
...
You win! The word was: apple
```

### 🛠️	Optional Enhancements

#### Description
Add one or more optional features to improve usability, reusability, or challenge.

#### Requirements
Completed program may include any of the following (implement at least one to get bonus credit):

- Read the word list from a text file (one word per line) and handle file-read errors gracefully.
- Show a list of letters already guessed (correct and incorrect) each turn.
- Implement difficulty modes that adjust the number of attempts or choose longer/shorter words.
- Provide a hint system (e.g., reveal one random unrevealed letter) limited to a small number of uses.

Example enhancement: load words from "words.txt" and show guessed letters:
```
Guessed letters: a, e, s, t
Current word: _ a _ _ _
```
