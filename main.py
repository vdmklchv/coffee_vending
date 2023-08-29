from finance import *
from menu import MENU
from error import ItemError, NotEnoughResourcesError
from processor import get_drink_price, has_enough_resources_for, make_drink
from screen import show_menu, show_report


def main():
    machine_on: bool = True
    total_profit: float = 0

    while machine_on:
        user_choice = show_menu()
        if user_choice.lower() == "report":
            show_report(total_profit)
        elif user_choice.lower() == "off":
            machine_on = False
            print("Turning off. Bye...")
        else:
            try:
                print(f"The cost of {user_choice} is ${get_drink_price(user_choice)}.")
                money = calculate_user_money(get_user_money())
                if has_enough_money(money, user_choice) and has_enough_resources_for(user_choice):
                    make_drink(user_choice)
                    drink_price = MENU[user_choice]["cost"]
                    print(f"Here is ${calculate_change(drink_price, money):.2f} dollars in change.")
                    print(f"Here is your {user_choice}, enjoy your drink!")
                    total_profit += drink_price
                else:
                    print("Sorry that's not enough money. Money refunded.")
            except ItemError as e:
                print(e)
            except NotEnoughResourcesError as e:
                print(e)


if __name__ == "__main__":
    main()
