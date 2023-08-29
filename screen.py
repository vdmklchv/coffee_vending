from error import ItemError
from menu import resources


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
