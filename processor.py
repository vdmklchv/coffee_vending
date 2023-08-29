from error import ItemError, UnknownIngredientError, NotEnoughResourcesError
from menu import MENU, resources


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


def make_drink(drink_name: str) -> None:
    """Checks if resources enough and makes a drink or gives error."""
    try:
        if has_enough_resources_for(drink_name):
            withdraw_resources_for(drink_name)
        else:
            raise NotEnoughResourcesError(f"Not enough resources to make this drink.")
    except UnknownIngredientError as error:
        print(error)