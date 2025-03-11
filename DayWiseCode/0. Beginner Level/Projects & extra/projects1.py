# Step 1
# Write Algorithm steps
# Loop
    # Ask : roll the dice?
    # If user enters y:
        # generate two random numbers (1,6) 
        # print the numbers
    # elif user enters n:
        # print Thank your for playing!
        # terminate
    # else:
        # Print Invalid input / please checkyour input and try agian
  
# Step 2      
# Create a flow chart for your algorithm



# Step 3
# Start Writing Code

# You should must focus on the below steps
    # Modularization (break down / reducing code / simplifying code)
    # Modularization ==> modules creating
    # DRY ==> Don't Repeat Yourself

import random

# while True:
#     print("Hello")
#     break

while True:
    user_asking = input("Do you want to 'Roll the Dice?' Press 'Y' to play or 'N' for to exit => ").lower()
    if user_asking == 'y':
        computer_choice1 = random.randint(1,6)
        computer_choice2 = random.randint(1,6)
        print(f"first_dice: {computer_choice1} \n second_dice: {computer_choice2} ") #string concation // f-string
    elif user_asking == 'n':
        print("Thank your for playing!")
        break
    else:
        print("Invalid input! try agian ")
        
        
