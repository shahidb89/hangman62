import random
class Hangman:
     '''
     """
    A class to represent the Hangman game.

    Attributes
    ----------
    word : str
        The word to guess, chosen randomly from the word list.
    word_guessed : list of str
        A list of the letters of the word, with _ for each letter not yet guessed. 
        For example, if the word is 'apple', the word_guessed list would be 
        ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters : int
        The number of unique letters remaining to be guessed.
    num_lives : int
        The number of lives the player has left.
    word_list : list of str
        The list of words give to the computer to randomly choose from.
    list_of_guesses : list of single letter str
        The list of single letter guesses made by the player.
    '''
    def __init__(self, word_list, num_lives=5):
        """
        See help(Hangman) for accurate signature.
        """
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        """
        Checks if a guessed letter is in the word.

        Parameters
        ----------
        guess : str
            The letter guessed by the player.

        Prints
        ------
        str
            Message indicating whether the guess was correct or incorrect.
        """
        guess = guess.lower() #Converts input to lower case for compatibility.
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            #for loop replaces every '_' in the word_guessed listed to the matched letter.
            for i, letter in enumerate (self.word):
                if letter == guess:
                    self.word_guessed[i] = letter
            self.num_letters -= 1 #reduces number of unknown unique letters by 1. 
        else:
            self.num_lives -= 1 
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives lseft')


    def ask_for_input(self):
        """
        Prompts the player to guess a letter, checks input validity, and processes the guess.
        For the input to be valid, it should be a single letter, otherwise, the user would be 
        prompted again until a valid single letter is entered.
        """
        while True:
            guess = input('Enter a single letter: ')
            if not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
    
def play_game(word_list):
    """
    Initiates and manages the Hangman game loop.

    Parameters
    ----------
    word_list : list of str
        The list of words give to the computer to randomly choose from.

    Prints
    ------
    str
        Game result, indicating if the player won or lost.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
             game.ask_for_input()
             print(game.word_guesseda)
        else:
            print("Congragulations. You won the game!")
            break

word_list = ["apple", "banana", "orange", "plum", "peach"]


play_game(word_list)

