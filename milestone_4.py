import random
class Hangman:
    def __init__(self, world_list, num_lives):
        word.self = random.choice(world_list)
        word_guessed.self = ['_' for letter in word.self]
        num_letters.self = len(set(word))
        num_lives.self = 5
        world_list.slef = world_list
        list_of_guesses.self = []
        
    def check_guess(self, guess):
        guess.lower()
        if guess in word.self:
            print(f'Good guess! {guess} is in the word.')

    def ask_for_input():
        while True:
            guess = input('Enter a single letter: ')
            if not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in list_of_guesses.self:
                print('You already tried that letter!')
            else:
                check_guess(guess)
        return list_of_guesses.self.append(guess)

Hangman.ask_for_input()