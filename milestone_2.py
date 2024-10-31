import random

word_list = ["apple", "banana", "orange", "plum", "peach"]
# for word in word_list:
#     print (word)

word = random.choice(word_list)

# print(word)
if __name__ ==   "__main__":
    guess = input("Enter a single letter: ")

    if len(guess) == 1 and guess.isalpha():
        print('Good guess!')
    else:
        print('Oops! That is not a valid input.')