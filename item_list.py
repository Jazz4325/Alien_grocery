from items import *

# ---------------------------- EDIBLE ----------------------------

    # -------------- foods --------------

class BeefJerky(Snack):
    
    name = "Jack's Links Beef Jerky"
    material = {
        "plastic" : 25, 
        }
    nutrition = {
        "Fat (g)" : 1.5,
        "Cholesterol (mg)" : 40,
        "Sodium (mg)" : 740,
        "Carbohydrate (g)" : 6,
        "Dietary Fiber (g)" : 0,
        "Sugar (g)" : 5,
        "Protein (g)" : 15,
        "Iron (% DV)" : 8,
        "Vitamin D (% DV)" : 0,
        "Calcium (% DV)" : 0,
        }
    value = 3.99
    description = "Power up with this meaty snack. The taste and texture might not be the best, but it's loaded with protein."

class Twinkie(Sweets):
    
    name = "Twikie"
    material = {
        "plastic" : 15, 
        }
    nutrition = {
        "Fat (g)" : 1.9,
        "Cholesterol (mg)" : 35,
        "Sodium (mg)" : 370,
        "Carbohydrate (g)" : 44,
        "Dietary Fiber (g)" : 0,
        "Sugar (g)" : 28,
        "Protein (g)" : 2,
        "Iron (% DV)" : 1,
        "Vitamin D (% DV)" : 0,
        "Calcium (% DV)" : 0,
        }
    value = 2.49
    description = "A delicacy for nearly a century, these sweet treats are sure to delight any who try them."

class CheeseStick(PerishableGrocery):
    
    name = "String Cheese"
    material = {
        "plastic" : 10, 
        }
    nutrition = {
        "Fat (g)" : 6,
        "Cholesterol (mg)" : 15,
        "Sodium (mg)" : 200,
        "Carbohydrate (g)" : 0,
        "Dietary Fiber (g)" : 0,
        "Sugar (g)" : 0,
        "Protein (g)" : 7,
        "Iron (% DV)" : 0,
        "Vitamin D (% DV)" : 0,
        "Calcium (% DV)" : 15,
        }
    value = 2.99
    description = "Peel off a couple strings of this cheesy treat - Comes in many flavors."

    # -------------- drinks --------------

class PabstBlueRibbon(Alcohol):
    
    name = "Pabst Blue Ribbon"
    material = {
        "metal" : 25, 
        }
    nutrition = {
        "Fat (g)" : 1,
        "Cholesterol (mg)" : 0,
        "Sodium (mg)" : 25,
        "Carbohydrate (g)" : 5,
        "Dietary Fiber (g)" : 0,
        "Sugar (g)" : 3,
        "Protein (g)" : 0,
        "Iron (mg)" : 0,
        "Vitamin D (mcg)" : 0,
        "Calcium (mg)" : 0,
        }
    value = 3.19
    ABV = 4.7
    description = "A tallboy of the good stuff! When work gets you down, chug a couple and forget your worries."

class CanOfSoda(Soda):
    
    name = "Can of Coca-Cola"
    material = {
        "metal" : 15, 
        }
    nutrition = {
        "Fat (g)" : 0,
        "Cholesterol (mg)" : 0,
        "Sodium (mg)" : 45,
        "Carbohydrate (g)" : 39,
        "Dietary Fiber (g)" : 0,
        "Sugar (g)" : 39,
        "Protein (g)" : 0,
        "Iron (mg)" : 0,
        "Vitamin D (mcg)" : 0,
        "Calcium (mg)" : 0,
        }
    value = 1.49
    description = "This sweet beverage helps to get the average worker through their shift with its high sugar levels."

class EarlGrey(CoffeeTea):

    name = "Cup of Earl Grey Tea"
    material = {
        "plastic" : 10, 
        }
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
    value = 0.99
    Caffeine = 45
    description = "Relax and take of sip of this piping hot beverage. Devoid of any nutrition, only sophisticated individuals enjoy this bitter drink."

class Gatorade(SportsDrink):
   
    name = "Cup of Earl Grey Tea"
    material = {
        "plastic" : 20, 
        }
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
    value = 0.99
    description = "Relax and take of sip of this piping hot beverage. Devoid of any nutrition, only sophisticated individuals enjoy this bitter drink."

# ---------------------------- INEDIBLE ----------------------------

    # -------------- vices --------------

class Cigarette(Vices):
    
    name = "Lucky Strike"
    material = {
        "plastic" : 5,
        }
    value = 9.99
    description = "Have a long drag of a soothing cancer stick. It's bound to relax and motivate you."

    # -------------- cosmetics/toiletries --------------

class HandSanitizer(CosmeticsToiletries):
    
    name = "Purell Hand Sanitizer"
    material = {
        "plastic" : 40, 
        }
    value = 6.99
    description = "Clean off those hands, if only marginally. Will do in a pinch to kill germs."

    # -------------- stationary --------------

class Newspaper(Stationary):
    
    name = "The Oregonian"
    material = {
        "plastic" : 5
        }
    value = 2.49
    description = "Pick up a daily copy and catch up on local news and well as the international intrigue."

    # -------------- comforts --------------

class HandWarmer(Comforts):
    
    name = "Hand Warmers"
    material = {
        "plastic" : 15
        }
    value = 1.99
    description = "Warm up your hands on a cold day - these shakable pads really save the day sometimes."

    # -------------- cleaning supplies --------------

class Bleach(CleaningSupplies):

    name = "OxiClean"
    material = {
        "plastic" : 45
        }
    value = 4.99
    description = "Careful not to get any in your eye - this powerful bleaching agent will clean any stain."

# ---------------------------- STORE INFRASTRUCTURE ----------------------------

    # -------------- machines --------------

class ATM(CustomerFacing):
    
    name = "ATM"
    material = {
        "metal" : 245, 
        }
    description = "If you need to grab cash in a pinch, this machine will do the trick."
        
class Register(EmployeeOnly):
    
    name = "Cash Register"
    material = {
        "metal" : 75, 
        }
    description = "Where the employees hold the money. Better not get caught with your hand in the till, thats a crime!"

    # -------------- storage --------------

class Freezer(Storage):
    
    name = "Industrial Freezer"
    material = {
        "metal" : 1215, 
        "plastic" : 445,
        "rubber" : 100
        }
    description = "This massive industrial freezing unit is built to last, keeping food reliably frozen 24/7."

class ShelvingUnit(Storage):
    
    name = "Commercial Shelving Unit"
    material = {
        "metal" : 625, 
        "plastic" : 205,
        "rubber" : 55
        }
    description = "Pretty much everything in the store that isnt in a fridge or freezer is sitting on one of these."

# ---------------------------- EQUIPMENT ----------------------------

    # -------------- medicine --------------

class HealthShot(Medicine):
    
    name = "Hp Syringe"
    material = {
        "plastic" : 10, 
        "metal" : 5
        }
    Dosage = 15
    description = "15cc's of alien drugs, stright to the vein - that'll restart even an elephant's heart."

    # -------------- weapons --------------

class Pistol(Ranged):
    
    name = ".45 Colt"
    material = {
        "metal" : 85, 
        "rubber" : 20
        }
    Range = 25
    Ammo = 24
    Damage = 10
    description = "Standard issue for Police Officers. Don't get in the way unless you want to be blasted."

class Taser(Melee):
    name = "Taser"
    material = {
        "metal" : 55, 
        "plastic" : 15
        }
    Damage = 0
    description = "Use this to subdue an enemy without injuring them. Highly effective and used by police."

    # -------------- armor --------------

class BulletproofVest(Armor):
    name = "Kevlar Vest"
    material = {
        "metal" : 125, 
        "plastic" : 35,
        "rubber" : 40
        }
    Armor_Class = 3
    description = "Struck by a bullet? Fear not! This standard issue vest has saved the lives of many officers on duty."

# --------------------------------------- print testing --------------------------------------- 

coke = CanOfSoda()
pbr = PabstBlueRibbon()
tea = EarlGrey()

jerky = BeefJerky()
twinkie = Twinkie()
cheese = CheeseStick()

cig = Cigarette()
sani = HandSanitizer()
news = Newspaper()
hand_warmer = HandWarmer()
bleach = Bleach()

freezer = Freezer()
shelf = ShelvingUnit()

hp_shot = HealthShot()
pistol = Pistol()
taser = Taser()
vest = BulletproofVest()

print("-------------------------------------------- DRINKS --------------------------------------------")
print(coke)  
print(pbr)
print(tea)
print("-------------------------------------------- FOODS --------------------------------------------")
print(jerky)
print(twinkie)
print(cheese)
print("-------------------------------------------- INEDIBLE --------------------------------------------")
print(cig)
print(sani)
print(news)
print(hand_warmer)
print(bleach)
print("-------------------------------------------- INFRASTRUCTURE --------------------------------------------")
print(freezer)
print(shelf)
print("-------------------------------------------- EQUIPMENT --------------------------------------------")
print(hp_shot)
print(pistol)
print(taser)
print(vest)
