#JUST MESSIN AROUND
'''
from items import Edible

class Interactable:
    def action():
        pass


class VendingMachine(Interactable):
    pass

class FuckYHouMyTHingDOFSJL(Interactable):
    pass


class Player:
    def __init__(self, name):
        self.name = name
        self.stomach_contents = {}

    def interact(self, other: Interactable):
        other.action()

    def use(self, item):
        if isinstance(item, Edible):
            for nutrient, amount in item.nutrients.items():
                if nutrient in self.stomach_contents:
                    self.stomach_contents[nutrient] += amount
                else:
                    self.stomach_contents[nutrient] = amount
        else:
            item.use()
        


#  items() { } -> [     
#   (key, value)
#   (key, value)
#   ]
# https://docs.python.org/3/library/stdtypes.html#dict.items


my_list = [1, 2, 3, 4, 5]

(ele_1, ele_2) = my_list


for (nutrient, amount) in item.nutrients.items():

for nutrient in item.nutrients:
    amount = item.nutrients[nutrient]

for nutrient in item.nutrients.keys():
    amount = item.nutrients[nutrient]
'''