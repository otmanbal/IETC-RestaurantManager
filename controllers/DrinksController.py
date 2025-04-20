from models.Drinks import Drinks

LstDrink = []

def AddDrink(id, name, ingredients, price):
    """
    Cette fonction permet d'ajouter une boisson au menu.
    """
    drink = Drinks(id, name, ingredients, price)
    LstDrink.append(drink)
    return


def RemoveDrink(id):
    """
    Cette fonction permet de supprimer une boisson du menu.
    """
    for drink in LstDrink:
        if drink.id == id:
            LstDrink.remove(drink)
        return


def ModifyDrink(id, name=None, ingredients=None, price=None):
    """
    Cette fonction permet de modifier une boisson du menu.
    """
    for drink in LstDrink:
        if drink.id == id:
            if name:
                drink.name = name
            if ingredients:
                drink.ingredients = ingredients
            if price:
                drink.price = price
            return


def ReadDrink(id, name, ingredients, price):
    """
    Cette fonction permet de lire une boisson du menu.
    """
    for drink in LstDrink:
        if drink.id == id:
            print(f"Name: {drink.name}, Ingredients: {drink.ingredients}, Price: {drink.price}")
        return