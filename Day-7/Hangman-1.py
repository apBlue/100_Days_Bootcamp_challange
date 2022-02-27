#Step 1

word_list = ["aardvark", "baboon", "camel"]

#1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

guess= random.choice(word_list)

# Driver code


User_ask= str(input("Guess a letter: "))

user_ask_lower= User_ask.lower()
for i in guess:
    if i == user_ask_lower:
        print("Right")
    else:
        print("Wrong")
