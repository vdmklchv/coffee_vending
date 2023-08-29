from error import ItemError
from menu import MENU
from processor import get_drink_price


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


def calculate_change(needed_money: float, user_money: float) -> float:
    """Calculates needed amount of change after the drink is made"""
    return user_money - needed_money
