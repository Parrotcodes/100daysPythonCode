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


is_on = True
while is_on:
    user_choice = input(f"What would you like? ({resource_keys()}):")

    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        available_resource()
        item_cost()
    else:
        drink = MENU[user_choice]
        print(drink)