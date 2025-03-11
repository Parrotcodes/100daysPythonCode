# Number Guessing Game

# Algorithm

# Generate a random ===> (5)
# Ask: guess a number between 1 to 100 ===> (50) / (2) / #else 200 / k --> error
# try
    # ifcomputer_number < guessing_number: ==> 5 < 50
        # Print your number is too high
    # elif computer_number > guessing_number: 2 < 5
        # Print Your number is Too low
# except
    # Invalid input 


    
# writing code

# try / except
import random

computer_choice = random.randint(1,100)

while True:
    
    guess_num = int(input("Guess a number between 1 to 100 "))
    
    try:
        if computer_choice < guess_num: 
            print("your number is too high")
            
        elif computer_choice > guess_num: 
            print("your number is too low")
            
        else:
            print("Congratulations! You guessed the correct number")
            break        
    except ValueError:
        print("Invalid guessing number")




    