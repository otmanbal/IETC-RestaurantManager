from models.Starter import Starter

LstStarter = []

def AddStarter(id, name, ingredients, price):
    """
    Cette fonction permet d'ajouter une entrée au menu.
    """
    starter = Starter(id, name, ingredients, price)
    LstStarter.append(starter)
    return


def RemoveStarter(id):
    """
    Cette fonction permet de supprimer une entrée du menu.
    """
    for starter in LstStarter:
        if starter.id == id:
            LstStarter.remove(starter)
        return


def ModifyStarter(id, name=None, ingredients=None, price=None):
    """
    Cette fonction permet de modifier une entrée du menu.
    """
    for starter in LstStarter:
        if starter.id == id:
            if name:
                starter.name = name
            if ingredients:
                starter.ingredients = ingredients
            if price:
                starter.price = price
            return


def ReadStarter(id, name, ingredients, price):
    """
    Cette fonction permet de lire une entrée du menu.
    """
    for starter in LstStarter:
        if starter.id == id:
            print(f"Name: {starter.name}, Ingredients: {starter.ingredients}, Price: {starter.price}")
        return