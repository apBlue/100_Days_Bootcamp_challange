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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



"""
######################### My Code works but there is bug i need to fix #########################################


# Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

def user_money():
    quarters = int(input("how many quaters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return quarters, dimes, nickels, pennies


# Turn off the Coffee Machine by entering “off” to the prompt.
coffee_machine = True
money = 0


# Print report


# Check resources sufficient?


# Process coins.
def calculate_money(quarters, dimes, nickels, pennies):
    quarter = quarters * 0.25
    dime = dimes * 0.10
    nickel = nickels * 0.05
    penny = pennies * 0.01
    Total = quarter + dime + nickel + penny
    return Total


# Check transaction successful?
while coffee_machine:
    ask_user = input("What would you like? (espresso/latte/cappuccino): ").lower()
    print("Please insert coins.")
    quarters, dimes, nickels, pennies = user_money()
    Total_value = calculate_money(quarters, dimes, nickels, pennies)
    if ask_user == "off":
        coffee_machine = False



    # Print report

    elif ask_user == "report":
        print(
            f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}\nMoney: ${money}')

    elif ask_user == "latte":

        # Check resources sufficient?

        if resources["water"] > 200 and resources["milk"] > 150 and resources["coffee"] > 24:


            if Total_value > MENU["latte"]["cost"]:
                remaining_value = Total_value - MENU["latte"]["cost"]
                money += MENU["latte"]["cost"]
                print(f"Here is {remaining_value} in change.")
                print("Here is your latte ☕. Enjoy!")
                resources["water"] -= 200
                resources["milk"] -= 150
                resources["coffee"] -= 24

                # Check transaction successful
            else:
                print("Sorry that's not enough money. Money refunded.")

        elif resources["water"] < 200:
            print("Sorry there is not enough water.")

    elif ask_user == "espresso":

        # Check resources sufficient?

        if resources["water"] > 50 and resources["coffee"] > 18:

            if Total_value > MENU["espresso"]["cost"]:
                remaining_value = Total_value - MENU["espresso"]["cost"]
                money += MENU["espresso"]["cost"]
                print(f"Here is {remaining_value} in change.")
                print("Here is your espresso ☕. Enjoy!")
                resources["water"] -= 50
                resources["coffee"] -= 24

                # Check transaction successful
            else:
                print("Sorry that's not enough money. Money refunded.")

        elif resources["water"] < 50:
            print("Sorry there is not enough water.")

    elif ask_user == "cappuccino":

        # Check resources sufficient?

        if resources["water"] > 250 and resources["milk"] > 100 and resources["coffee"] > 24:

            if Total_value > MENU["cappuccino"]["cost"]:
                remaining_value = Total_value - MENU["latte"]["cost"]
                money += MENU["cappuccino"]["cost"]
                print(f"Here is {remaining_value} in change.")
                print("Here is your cappuccino ☕. Enjoy!")
                resources["water"] -= 250
                resources["milk"] -= 100
                resources["coffee"] -= 24

            # Check transaction successful

            else:
                print("Sorry that's not enough money. Money refunded.")

        elif resources["water"] < 250:
            print("Sorry there is not enough water.")

"""
