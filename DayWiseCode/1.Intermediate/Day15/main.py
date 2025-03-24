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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")

    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        for item in resources:
            print(f"{item} : {resources[item]}")
        print(f"Money : {profit}")
    else:
        drink = MENU[user_choice]
        print(drink)