# Menu Data
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
# Resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Coffe Machine Methods
def available_resource():
    for i in resources:
        print(f"{i} : {resources[i]}")
    return True

def item_cost():
    print(f"Money : {profit}")
    return True

def resource_keys():
    for i in MENU:
        return f"{i}/{i}/{i}"

def is_resource_sufficent(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """ Returns the total calculated coins form coins inserted """
    print("Please Insert coins")
    total = int(input("How many quarters? $")) * 0.25
    total += int(input("How many dimes? $")) * 0.10
    total += int(input("How many nickels? $")) * 0.05
    total += int(input("How many pennies? $")) * 0.01
    return total

def is_transaction_successful(payment_recieved,drink_cost):
    if payment_recieved >= drink_cost:
        print(f"Drink Cost: {round(drink_cost,2)}")
        print(f"Money recieved: {round(payment_recieved,2)}")
        change = round(payment_recieved - drink_cost,2)
        print(f"Here is your Change amount: ${change} in change.")
        global profit
        profit += drink_cost
        print("your service is provided successfully!")
        return True
    else:
        print(f"Money received: {payment_recieved}")
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffe(drink_name,ordered_ingredaints):
    """ Deduct the required ingredients from the resources. """
    for item in ordered_ingredaints:
        resources[item] -= ordered_ingredaints[item]
    print(f"Here is your {drink_name} 🍵.")


# Code Start here
is_on = True
while is_on:
    # user_choice = input(f"What would you like? ({resource_keys()}):")
    user_choice = input(f"What would you like? (espresso/latte/cappuccino):")

    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        available_resource()
    else:
        drink = MENU[user_choice]
        # print(drink)
        if is_resource_sufficent(drink["ingredients"]):
            payment = process_coins()
            # print(f"Cost: {payment}")
            # is_transaction_successful(payment,drink["cost"])
            if is_transaction_successful(payment,drink["cost"]):
                make_coffe(user_choice,drink["ingredients"])

