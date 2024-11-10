# Hangman

A simple, computer based implementation of the Hangman game.

## Description

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Usage Instructions
To Run the game, ensure you have Python 3 installed. Download the hangman.py file and execute the script in the Command Line Terminal as the following:

```bash
python hangman.py

or 

./hangman.py
```

Otherwise, you can open the file, or copy the scripts to a Jupyter Notebook and run the code.

## How to Play
1. The game randomly selects a word from a predefined list of words.
2. The player has a fixed number of lives (default is 5).
3. The player is prompted to guess one letter at a time.
4. If the guessed letter is in the word, it is revealed in the correct position(s).
5. If the guessed letter is not in the word, the player loses a life.
6. The game continues until either:
   - The player correctly guesses all letters in the word (win).
   - The player runs out of lives (loss).


## Code Structure

### Class: `Hangman`

The main class that handles the game logic and user interactions.

- **Attributes**:
  - `word`: The secret word the player has to guess.
  - `word_guessed`: A list showing the current state of the guessed word.
  - `num_letters`: Number of unique letters remaining to be guessed.
  - `num_lives`: The player's remaining lives.
  - `word_list`: List of potential words for the game.
  - `list_of_guesses`: List of letters guessed by the player.

- **Methods**:
  - `__init__(word_list, num_lives=5)`: Initializes the game with a word list and starting lives.
  - `check_guess(guess)`: Checks if a guessed letter is in the word and updates game status.
  - `ask_for_input()`: Prompts for player input and processes the guess.

### Function: `play_game`

The main function that initializes a game instance and runs the game loop.

- **Parameters**:
  - `word_list`: A list of words from which the game randomly selects the target word.


## Requirements
* Python 3.x
* No additional requirements.

## License
This project is licensed under the MIT License.