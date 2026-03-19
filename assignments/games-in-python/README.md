# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. In this assignment, you will practice managing game state and creating a complete interactive program.

## 📝 Tasks

### 🛠️ Set Up the Game State

#### Description
Use the starter code to prepare the Hangman game before play begins. Choose a secret word from the provided list and create the variables needed to track guesses and remaining attempts.

#### Requirements
Completed program should:

- Randomly select one word from the predefined `words` list.
- Create variables to store guessed letters, the number of incorrect guesses, and the maximum number of incorrect guesses allowed.
- Display the hidden word using underscores for letters that have not been guessed yet.


### 🛠️ Complete the Game Loop

#### Description
Finish the main game loop so the player can guess letters until they either reveal the full word or run out of attempts.

#### Requirements
Completed program should:

- Ask the player to enter one letter at a time.
- Update the displayed word when the guess is correct.
- Decrease the remaining attempts when the guess is incorrect.
- End the game when the word is fully guessed or the player has no attempts left.
- Display a clear win message if the player guesses the word and a clear lose message if they do not.
