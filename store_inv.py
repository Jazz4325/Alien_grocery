from item_list import *

class Department():

    def __init__(self, name, stock={}):
        self.name = name
        self.stock = stock

    # we are not initing items here, we are only making a blueprint of what can/cannot be in a specific department when IT is inited
    
    # method to add_stock / restock? / update_stock once department is already inited
    
    def check_stock(self, item_class_name):
        print(f"checking if {item_class_name} is in stock...")
        if item_class_name in self.stock:
            item_count = self.stock[item_class_name]
            # [item_class_name] uses the value of item_class_name as a key to look up the corresponding value in the dictionary.
            # That value (the number in stock) is retrieved and assigned to item_count.
            print(f"there are {item_count} in stock.")
            return item_count
        else:
            print(f"{self.name} doesn't carry {item_class_name}... check another department?")
            return 0
    
    def take_item(self, item_class_name):
        if self.check_stock(item_class_name) > 0:
            item = item_class_name()
            # using item_class_name as a function calls init on that item, spawning it
            print(item)
            self.stock[item_class_name] -= 1    
            return item
        else:
            print(f"there are no {item_class_name}'s in stock...")