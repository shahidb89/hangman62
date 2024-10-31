import milestone_2
while True:
    guess = input("Enter a single letter: ")
    if len(guess)==1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in milestone_2.word:
    print(f"Good guess!  is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")  
