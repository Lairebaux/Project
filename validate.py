from items_menu import *
from functools import wraps

# data class instance
data = Data()

def _while_loop(func):
    @wraps(func)
    def wrapper(*args):
        """while loop decorator"""
        looping = True
        while looping:
            try:
                f = func(*args)
            except ValueError as err:
                print("\n", err)
            else:
                looping = False
        return f
    return wrapper


@_while_loop
def validate_food_order():
    """
    Access flavour menu based on food chosen
    Returns flavour chosen
    """
    display_food_menu()
    print("What would you like to order? ")
    choice = validate_item()
    if choice != "c" and choice != "p":
        return choice
    if choice == "c":
        display_chips_menu()
    else:
        display_popcorn_menu()
    print("Which Flavour? ")
    flavour = validate_flavour(choice)
    return flavour


@_while_loop
def validate_flavour(choice):
    """returns flavour according to chips or popcorn"""
    flav = input("--> ").lower()
    if choice == "c":
        if flav not in data.chips:
            raise ValueError("Please choose appropriate flavour.")
    else:
        if flav not in data.popcorn:
            raise ValueError("Please choose appropriate flavour.")
    return flav


def validate_item():
    """return choice if in lists"""
    choice = input("->: ")
    if choice not in data.food_items and choice not in ["c", "p"]:
        raise ValueError("Please select an item from the menu.")
    return choice


@_while_loop
def anything_else():
    """return y or n"""
    print('\nAnything else (y) or (n)?\n')
    answer = input("-> ").lower()
    if answer not in ("y", "n"):
        raise ValueError("Please choose y or n.")
    return answer


@_while_loop
def validate_amount():
    """validates value between 1 and 10 inclusively"""
    value = int(input("How many: "))
    if value < 1 or value > 10 :
        raise ValueError("Please choose an amount between 1 and 10.")
    return value


def customer_food_order():
    """ :returns food order item and amount"""
    item = validate_food_order()
    amount = validate_amount()
    return (item, amount)


