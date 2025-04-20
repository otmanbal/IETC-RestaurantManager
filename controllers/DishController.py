from models.Dish import Dish

LstDish = []

def AddDish(id, name, ingredients, price):
    """
    Cette fonction permet d'ajouter un plat au menu.
    """
    dish = Dish(id, name, ingredients, price)
    LstDish.append(dish)
    return


def RemoveDish(id):
    """
    Cette fonction permet de supprimer un plat du menu.
    """
    for dish in LstDish:
        if dish.id == id:
            LstDish.remove(dish)
        return


def ModifyDish(id, name=None, ingredients=None, price=None):
    """
    Cette fonction permet de modifier un plat du menu.
    """
    for dish in LstDish:
        if dish.id == id:
            if name:
                dish.name = name
            if ingredients:
                dish.ingredients = ingredients
            if price:
                dish.price = price
        return
    

def ReadDish(id, name, ingredients, price):
    """
    Cette fonction permet de lire un plat du menu.
    """
    for dish in LstDish:
        if dish.id == id:
            print(f"Name: {dish.name}, Ingredients: {dish.ingredients}, Price: {dish.price}")
        return