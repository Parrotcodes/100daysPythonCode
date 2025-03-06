# Hangman Project

# Solution Steps:

import random
import ProModuleDiag
import listofwords

health = 6

# Task 1
# step1: create a list of items

# import listofwords
# list_of_words = ["apple", "banana", "mango", "grapes", "orange", "kiwi", "watermelon", "papaya", "guava", "pineapple"]
Selected_word = listofwords.mywords_list
# step2: select random word every time from the list
Choosen_word = random.choice(Selected_word)
print(Choosen_word)


# generate the blanks for the choosen word
# apple = _ _ _ _ _
display = []
# print(f"Empty list: {display}")
for newblank in range(len(Choosen_word)):
    display += "_"
# print(f"Updated list: {display}" )
print(display)


# step3:input = guess a letter from the list

while "_" in display and health > 0:
    guess = input("Guess a letter: ").lower()
    print(guess)
    # step4: check the guess one of the letter in the choosen word

    if guess in Choosen_word:
        # print("Yes")
        for indexPosition in range(len(Choosen_word)): # apple = a, p, p, l, e
            letter = Choosen_word[indexPosition] # apple = a
            if letter == guess:
                display[indexPosition] = letter # updated display = a _ _ _ _
        print(display)
            
        if "_" not in display: # apple = a, p, p, l, e
            print("You win")
    else:
        # print("No")
        health -= 1
        print(f"Health: {health}")
        print(ProModuleDiag.hangman_art[health])
        if health == 0:
            print("You lose")
            
               
        
# Task 2
# step1: display the no.of blanks == random seleted word letters

# step2: replace the letter at the correct position if the letter matched with the guessing letter
# display the replaced letters and remainig as blanks
# for indexPosition in range(len(Choosen_word)): # apple = a, p, p, l, e
#     letter = Choosen_word[indexPosition] # apple = a
#     if letter == guess:
#         display[indexPosition] = letter # updated display = a _ _ _ _
#         print(display)

# Task 3
# check the display blanks are no longer avalilable then print "you win"


# Task 4
# import all the symbols of hangman as a list 
# use random method and select the random list items from another list module


# Task 5
# Refer module section
# make better User experience
# Add logo
# add random words more / generate more (using module concept)
# remove the repetation of previous guessing letter / img