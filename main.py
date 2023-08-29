from menu import MENU, resources
from error import ItemError, NotEnoughResourcesError, UnknownIngredientError

MACHINE_ON = True
money = 0
total_profit = 0


def show_menu() -> str:
    """Ask and return user command"""
    return input("What would you like to do? (espresso/latte/capuccino/report/off) ").lower()


def format_report_item(item: str, amount: float) -> str:
    """Returns formatted string used to generate report"""
    if item == "money":
        return f"{item}: ${amount}"
    else:
        if item == "water" or item == "milk":
            measurement = "ml"
        elif item == "coffee":
            measurement = "g"
        else:
            raise ItemError("Item doesn't exist!")

        return f"{item.title()}: {amount}{measurement}"


def show_report(total_profit: float) -> None:
    """Logic to show report"""
    for item in resources:
        print(format_report_item(item, resources[item]))
    print(format_report_item("money", total_profit))


def get_drink_price(drink_name: str) -> float:
    """returns price for chosen drink"""
    if drink_name in MENU:
        return MENU[drink_name]["cost"]
    else:
        raise ItemError("Unknown drink.")


def get_drink_ingredients(drink_name: str) -> {str: int}:
    """returns ingredients for chosen drink"""
    if drink_name in MENU:
        return MENU[drink_name]["ingredients"]
    else:
        raise ItemError("Unknown drink.")


def has_enough_resources_for(drink_name: str) -> bool:
    """Return true if resources are enough to make a drink"""
    try:
        resources_needed = get_drink_ingredients(drink_name)
        for resource in resources_needed:
            if resource not in resources:
                raise UnknownIngredientError("Ingredient not known.")
            if resources_needed[resource] > resources[resource]:
                raise NotEnoughResourcesError(f"Sorry, not enough {resource}.")
        return True
    except ItemError as error:
        print(error)


def withdraw_resources_for(drink_name: str) -> None:
    """Withdraws resources for drink from machine"""
    try:
        required_resources = get_drink_ingredients(drink_name)
        for resource in required_resources:
            resources[resource] -= MENU[drink_name]["ingredients"][resource]
    except ItemError as error:
        print(error)


def insert_coins(coin_type: str) -> int:
    """Returns amount of inserted coins from user input"""
    coin_amount = None
    while type(coin_amount) is not int or coin_amount < 0:
        coin_amount = int(input(f"Insert {coin_type}: "))
    return coin_amount


def get_user_money() -> {str: {str: int}}:
    """Ask user to input coins of each type and return dictionary with coins"""
    quarters = insert_coins("quarters")
    dimes = insert_coins("dimes")
    nickels = insert_coins("nickels")
    pennies = insert_coins("pennies")

    return {
        "quarters": {
            "value": 0.25,
            "amount": quarters
        },
        "dimes": {
            "value": 0.1,
            "amount": dimes
        },
        "nickel": {
            "value": 0.05,
            "amount": nickels
        },
        "pennies": {
            "value": 0.01,
            "amount": pennies
        },
    }


def calculate_user_money(user_money: {str: {str: int}}) -> float:
    """Returns total amount of money inserted"""
    total = 0
    for coin in user_money:
        total += user_money[coin]["amount"] * user_money[coin]["value"]

    return total


def has_enough_money(user_money: float, drink_type: str) -> bool:
    """Returns True if user money is enough to buy chosen drink"""
    if drink_type in MENU:
        return user_money >= get_drink_price(drink_type)
    else:
        raise ItemError("Wrong item chosen.")


def make_drink(drink_name: str) -> None:
    """Checks if resources enough and makes a drink or gives error."""
    try:
        if has_enough_resources_for(drink_name):
            withdraw_resources_for(drink_name)
    except NotEnoughResourcesError as error:
        print(error)
    except UnknownIngredientError as error:
        print(error)


def calculate_change(needed_money: float, user_money: float) -> float:
    """Calculates needed amount of change after the drink is made"""
    return user_money - needed_money


while MACHINE_ON:
    user_choice = show_menu()
    if user_choice.lower() == "report":
        show_report(total_profit)
    elif user_choice.lower() == "off":
        MACHINE_ON = False
        print("Turning off. Bye...")
    else:
        try:
            print(f"The cost of {user_choice} is ${get_drink_price(user_choice)}.")
            money = calculate_user_money(get_user_money())
            if has_enough_money(money, user_choice):
                make_drink(user_choice)
                drink_price = MENU[user_choice]["cost"]
                print(f"Here is ${calculate_change(drink_price, money):.2f} dollars in change.")
                money = 0
                print(f"Here is your {user_choice}, enjoy your drink!")
                total_profit += drink_price
            else:
                print("Sorry that's not enough money. Money refunded.")
                money = 0
        except ItemError as e:
            print(e)
