menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def fill():
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100
    print("Replenishment completed.")


def resources_check():
    ingredients = menu[coffee]["ingredients"]

    for ingredient in ingredients:
        if not resources[ingredient] >= ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True


def coins_check():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total = round((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies), 2)

    price = menu[coffee]['cost']
    change = round((total - price),2)

    if total > price:
        print(f"Here is ${change} in change.")
        resources['money'] += price
        return True
    elif total == price:
        resources['money'] += price
        return True
    elif total < price:
        print("Sorry, that is not enough money. Money refunded.")
        return False


def transaction(check_1, check_2):
    ingredients = menu[coffee]["ingredients"]

    if check_1 and check_2:
        for ingredient in ingredients:
            resources[ingredient] -= ingredients[ingredient]

        print(f"Here is your {coffee}.")


coffee_machine = True

while coffee_machine:

    while True:
        coffee = input("What would you like (espresso/latte/cappuccino)? ").lower()
        if coffee == "espresso" or coffee == "latte" or coffee == "cappuccino" or coffee == "off":
            break
        elif coffee == "report":
            report()
        elif coffee == "fill":
            fill()

    if coffee == "off":
        break

    condition_1 = resources_check()

    if resources_check():
        condition_2 = coins_check()

    transaction(condition_1, condition_2)

