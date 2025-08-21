from item_list import *
from typing import Optional

StockType = dict[type, int]

class Department():

    def __init__(self, name, par: StockType={}):
        self.name = name
        self.par = par
        self.stock: StockType = {}
        self.restock_dept()

    # restock the whole dept to pars
    def restock_dept(self) -> None:
        for item_class_name in self.par:
            self.restock_item(item_class_name)

    # restock individual items 
    def restock_item(self, item_class_name) -> None:
        par_quantity = self.par[item_class_name]
        self.stock[item_class_name] = par_quantity
        
        """ restock specific subclasses
        for item_class_name in self.par:
            if isinstance(item_class_name, Edible):
                restock
        """

    # can the dept ever carry this item?
    def carries_item(self, item_class_name) -> bool: # type annotation!
        return item_class_name in self.stock # returns true if the thing is in stock, else returns false

    # if so, how many are there now?    
    def get_item_quantity(self, item_class_name) -> int:
        if not self.carries_item(item_class_name):
            return 0 
        return self.stock[item_class_name]

    # are there any of this item in this dept now?
    def item_in_stock(self, item_class_name) -> bool:
        return self.get_item_quantity(item_class_name) > 0
    
    def take_item(self, item_class_name) -> Optional[Item]:
        if self.item_in_stock(item_class_name):
            item = item_class_name()
            # using item_class_name as a function calls init on that item, spawning it
            print(item)
            self.stock[item_class_name] -= 1    
            return item
        else:
            print(f"there are no {item_class_name}'s in stock...")
    
