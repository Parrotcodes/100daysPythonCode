from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    # data
    ''' fromat the data and returns the printable fomat '''
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    # print("Compare A: Camila Cabello, a Musician, from Cuba.")
    return f"{account_name}, {account_desc}, from {account_country}"

def check_answer(guess, a_follwers, b_followers):
    if a_follwers > b_followers:
       return guess == "a"
    else:
       return guess == "b"    

print(logo)
score = 0
should_continue = True

# generate a random account form the data
account_b = random.choice(data)

# while repeats 
while should_continue:
    # print("Compare A: Camila Cabello, a Musician, from Cuba.")
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Comapre A: {format_data(account_a)}")

    print(vs)
    # print("Against B: Emma Watson, a Actress, from Uinted Kingdom.")
    print(f"Against B: {format_data(account_b)}")

    # ask the user
    guess = input("Who has more followers? Type 'A' or 'B'").lower()


    # check if user is correct
    ## get follwers count
    a_follwer_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follwer_count, b_follower_count)

    # clear the screen()
    # clear()
    os.system('cls||clear')    
    print(logo)

    ## count the score
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
    else:
        should_continue = False
        print(f"You're wrong! Your Final Score: {score}")
