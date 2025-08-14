class Item:
    
    name = ""
    material = {}
    description = ""

    def __init__(self):
        self.name = self.name
        self.material = self.material
        self.description = self.description

    def __str__(self):  
        
        # Format string and show subclass (MRO = Method Resolution Order)
        class_hierarchy = type(self).mro()[1:-1]
        category = next((cls.__name__ for cls in class_hierarchy if cls.__name__ != "Item"), "Uncategorized")

        lines = [
            f"{self.name} ({category})",
            f"{self.description}",
            ""
        ]

        if hasattr(self, 'value'):
            lines.append(f"Value: ${getattr(self, 'value')}")
        
        material_string = "\n  ".join(f"- {mat}: {amt}" for mat, amt in self.material.items())
        lines.append(f"Materials:\n  {material_string}")
        base_keys = {"name", "material", "description", "value"}
        attr_keys = (set(vars(self).keys()) | set(attr for attr in dir(self) if not attr.startswith('_'))) - base_keys
        attr_keys = {k for k in attr_keys if not callable(getattr(self, k))}

        for key in sorted(attr_keys):
            val = getattr(self, key)
            if isinstance(val, dict):
                lines.append(f"{key.capitalize()}:")
                for k, v in val.items():
                    lines.append(f"  - {k}: {v}")
            else:
                lines.append(f"{key}: {val}")
        
        return "\n".join(lines) + "\n"

# ---------------------------- EDIBLE ----------------------------

class Edible(Item):
    
    nutrition = {
        "Fat (g)" : 0,
        "Cholesterol (mg)" : 0,
        "Sodium (mg)" : 0,
        "Carbohydrate (g)" : 0,
        "Dietary Fiber (g)" : 0,
        "Sugar (g)" : 0,
        "Protein (g)" : 0,
        "Iron (mg)" : 0,
        "Vitamin D (mcg)" : 0,
        "Calcium (mg)" : 0,
        }
    value = 0

    # -------------- Foods --------------

class Food(Edible):
    
    def eat(self, item):
        pass

        # -------------- snacks -------------

class Snack(Food):
    pass

        # -------------- ready to eat ------------ todo: ABSTRACT FURTHER

class ReadyToEat(Food):
    pass
        
        # -------------- pg ------------

class PerishableGrocery(Food):
    pass

        # -------------- sweets ------------
    
class Sweets(Food):
    pass

    # -------------- Drinks --------------

class Drink(Edible):
    
    def drink(self, item):
        pass

        # -------------- non-alcoholic -------------

class NonAlcoholic(Drink):
    pass

            # -------------- soda -------------

class Soda(NonAlcoholic):
    pass

            # -------------- sports drinks ------------- 

class SportsDrink(NonAlcoholic):
    pass

            # -------------- coffee/tea ------------- 

class CoffeeTea(NonAlcoholic):
    
    Caffeine = 0

        # -------------- alcohol -------------

class Alcohol(Drink):
    
    ABV = 0.0

    def get_drunk(self, item):
        pass

# ---------------------------- INEDIBLE ----------------------------

class Inedible(Item):
    
    value = 0

    # -------------- cosmetics / toiletries --------------

class CosmeticsToiletries(Inedible):
    pass

    # -------------- comforts --------------

class Comforts(Inedible):
    pass

    # -------------- vices --------------

class Vices(Inedible):
    pass

    # -------------- cleaning supplies --------------

class CleaningSupplies(Inedible):
    pass

    # -------------- stationary --------------

class Stationary(Inedible):
    pass

# ---------------------------- STORE INFRASTRUCTURE ----------------------------

    # -------------- machine --------------

class Machine(Item):
    
    def turn_on(item):
        pass

    def turn_off(item):
        pass

    def tamper(item):
        pass
        
        # -------------- customer facing --------------

class CustomerFacing(Machine):
    pass

        # -------------- employees only --------------

class EmployeeOnly(Machine):
    pass

    # -------------- storage --------------

class Storage(Item):
    pass

        # -------------- fridge/freezer --------------

class FridgeFreezer(Storage):
    pass

        # -------------- shelf --------------

class Shelf(Storage):
    pass

# ---------------------------- EQUIPMENT ----------------------------

class Equipment(Item):
    pass

    # -------------- medicine --------------

class Medicine(Equipment):
    
    Dosage = 0

    # -------------- weapon --------------

class Weapon(Equipment):
    
    Damage = 0

        # -------------- ranged --------------

class Ranged(Weapon):
    
    Range = 0
    Ammo = 0

    def shoot(item):
        pass

    def point_at(item):
        pass

        # -------------- melee --------------

class Melee(Weapon):
    
    def swing(item):
        pass

    def brandish(item):
        pass

    # -------------- armor --------------

class Armor(Equipment):

    Armor_Class = 0