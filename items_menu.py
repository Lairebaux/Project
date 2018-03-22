from collections import namedtuple



class Data():
    def __init__(self, amount=None):

        food = namedtuple("food", "food price amount")
        chips = namedtuple("chips", "food_flavour price amount")
        popcorn = namedtuple("popcorn", "food_flavour price amount")


        self.food_items = {
                           "co": food("coffee", 2, amount),
                           "cc": food("cotton candy", 3, amount),
                           "hc": food("hot chocolate", 2, amount),
                           "ic": food("ice tea", 3, amount),
                           "j": food("juice", 2, amount),
                           "t": food("tea", 2, amount),
                           "w": food("water", 3, amount),
                           }

        self.chips = {
                          "q": chips("bbq chips", 2, amount),
                          "k": chips("ketchup chips", 2, amount),
                          "n": chips("natural chips", 2, amount),
                          "s": chips("salt & vinegar chips", 2, amount),
                         }

        self.popcorn = {
                          "b": popcorn("butter popcorn", 3, amount),
                          "c": popcorn("caramel popcorn", 3, amount),
                          "d": popcorn("cheddar popcorn", 3, amount),
                          "v": popcorn("salt & vinegar popcorn", 3, amount)
                         }



def display_food_menu():
    fm = "*** Food Menu ***"
    print("\n{0:>20}".format(fm))
    print(
        "(c)  chips           $2\n"
        "(cc) cotton candy    $3\n"
        "(co) coffee          $2\n"
        "(hc) hot chocolate   $2\n"
        "(ic) ice tea         $2\n"
        "(j)  juice           $2\n"
        "(p)  popcorn         $3\n"
        "(t)  tea             $3\n"
        "(w)  water           $3\n"
        )

def display_chips_menu():
    """print chips menu"""
    cm = "*** Chips Menu ***"
    print("{0:>20}".format(cm))
    print("Chips: Bb[Q], [K]etchup, [N]atural,  [S]alt & Vinegar\n")

def display_popcorn_menu():
    """print popcorn menu"""
    pm = "*** Popcorn Menu ***"
    print("{0:>20}".format(pm))
    print("Popcorn : [B]utter, [C]aramel, Che[d]dar, Salt & [V]inegar\n")
