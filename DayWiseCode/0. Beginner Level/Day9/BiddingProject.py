print("Welcome to the Secret Acution Program")

new_bidder = False
bids ={}
winner = ""

# This function is used for checking the highest bid_amount among all the bidders
def highest_Bidder(bidding_record):
    highest_price = 0 #21 100
    for bidder in [bidding_record]:
        if bid_amount > highest_price:
            highest_price  = bid_amount
        winner = bidder
    
    print(f"The winner is {winner} with a bid of {highest_price}")

# while loop continuously runnning based new_bidder condition
while not new_bidder:
    name = input("What is your name? ")
    bid_amount = int(input("What is your bid amount? $"))

    # {"rakesh": $21},{"raj" : $100}
    bids[name] = bid_amount
    
    ycontinue = input("Are there any other bidders? Type 'yes' or 'no' ")
    if ycontinue == "no":
        new_bidder = True 
        highest_Bidder(bids)  
    elif ycontinue == "yes":
        print("-------- clear screen -----")
        

