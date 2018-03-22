from validate import *
import os



def main():
    """Queries for another order; prints orders receipt """
    orders = []
    total = 0
    ordering = False
    while not ordering:
        item, amount = customer_food_order()
        data = Data(amount)
        if item in data.food_items:
            orders.append(data.food_items[item])
        elif item in data.chips:
            orders.append(data.chips[item])
        else:
            orders.append(data.popcorn[item])
        extras = anything_else()
        if extras == "n":
            ordering = True


    for items in orders:
        total += items[1] * items[2]
        # amount food price
        print(f"{items[2]} {items[0]:30}  {'@':<2} ${items[1]} each")
    print(f"\nYour total is ${total:0.2f}\nThank You!")





if __name__ == '__main__':
    main()

