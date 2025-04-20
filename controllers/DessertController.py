from models.Dessert import Dessert

LstDessert = []

def AddDessert(id, name, ingredients, price):
    """
    Cette fonction permet d'ajouter un dessert à la liste des desserts.
    """
    dessert = Dessert(id, name, ingredients, price)
    LstDessert.append(dessert)
    return


def RemoveDessert(id):
    """
    Cette fonction permet de supprimer un dessert de la liste des desserts.
    """
    for dessert in LstDessert:
        if dessert.id == id:
            LstDessert.remove(dessert)
        return


def ModifyDessert(id, name=None, ingredients=None, price=None):
    """
    Cette fonction permet de modifier un dessert de la liste des desserts.
    """
    for dessert in LstDessert:
        if dessert.id == id:
            if name:
                dessert.name = name
            if ingredients:
                dessert.ingredients = ingredients
            if price:
                dessert.price = price
            return


def ReadDessert(id, name, ingredients, price):
    """
    Cette fonction permet de lire un dessert de la liste des desserts.
    """
    for dessert in LstDessert:
        if dessert.id == id:
            print(f"Name: {dessert.name}, Ingredients: {dessert.ingredients}, Price: {dessert.price}")
        return