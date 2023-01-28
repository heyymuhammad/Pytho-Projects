MENU = {
    "chocolate": {
        "ingredients": {
            "chocolate": 100,
            "cream": 200,
            "milk": 300
        },
        "cost": 2.5
    },
    "vanila": {
        "ingredients": {
            "cream": 250,
            "milk": 300
        },
        "cost": 1.7
    },
    "pista": {
        "ingredients": {
            "pista": 50,
            "cream": 250,
            "milk": 300
        },
        "cost": 1.5
    },
    "banana": {
        "ingredients": {
            "banana": 100,
            "cream": 150,
            "milk": 300
        },
        "cost": 2.0
    }
}
resources = {
    "chocolate": 700,
    "pista": 200,
    "banana": 200,
    "cream": 1000,
    "milk": 1000
}
profit = 0


def is_resource_suf(order_ingredients):
    for item in order_ingredients:
        if resources[item] <= order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transaction_successfull(money_recieved, drink_cost):
    if money_recieved > drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} your change.")
        global profit
        profit += drink_cost
        return True
    else:
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} Ice Cream 🍨")


is_on = True

while is_on:
    choice = input("What would you like? (chocolate/pista/vanila/banana): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Cream: {resources['cream']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Chocolate: {resources['chocolate']}g")
        print(f"Pista: {resources['pista']}g")
        print(f"Banana: {resources['banana']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_suf(drink["ingredients"]):
            payment = process_coins()
            if transaction_successfull(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
