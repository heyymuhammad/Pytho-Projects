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

def is_resource_sufficient(order_ingredients):
    """Return True when order can be made and false when resource are not sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True       

def process_coins():
    """Return total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: $")) * 0.25
    total += int(input("How many dimes?: $")) * 0.1
    total += int(input("How many nickels?: $")) * 0.05
    total += int(input("How many pennies?: $")) * 0.01
    return total

def confirm_transaction(payment, item_cost):
    if payment >= item_cost:
        change = round(payment - item_cost, 2)
        print(f"Here is ${change} change.")
        global profit 
        profit+= item_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def update_resources(ingredients):
    global resources
    for item in ingredients:
        if item in resources:
            resources[item] -= ingredients[item]
    

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
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
            if confirm_transaction(payment, drink["cost"]):
                update_resources(drink["ingredients"])
                print(f"Here is your {choice} ☕")

            






































# def is_resource_suf(order_ingredients):
#     """ Returns True when order can be made, False if ingrdients are insufficient """
#     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True

# def process_coins():
#     """ Returns the total calculated from coins inserted"""
#     print("Please insert coins.")
#     total = int(input("How many quarters?: ")) * 0.25
#     total += int(input("How many dimes?: ")) * 0.1
#     total += int(input("How many nickles?: ")) * 0.05
#     total += int(input("How many pennies?: ")) * 0.01
#     return total


# def is_transaction_successfull(money_recieved, drink_cost):
#     """Return True when the payment is accepted, or False is money is sufficient."""
#     if money_recieved >= drink_cost:
#         change = round(money_recieved - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
 

# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingerdients from resources"""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕ ")

# is_on=True
# while is_on:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")
#     if choice =="off":
#         is_on = False
#     elif choice== "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink= MENU[choice]
#         if is_resource_suf(drink['ingredients']):
#             payment = process_coins()
#             if is_transaction_successfull(payment, drink['cost']):
#                 make_coffee(choice, drink['ingredients'])




