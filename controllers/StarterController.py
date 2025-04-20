from Starter import Starter

def AddStarter(self, id, name, ingredients, price):
    """
    Cette fonction permet d'ajouter une entrée au menu.
    """
    Starter = Starter(id, name, ingredients, price)
    self.LstStarter.append(Starter)
    return


def RemoveStarter(self, id):
    """
    Cette fonction permet de supprimer une entrée du menu.
    """
    for Starter in self.LstStarter:
        if Starter.id == id:
            self.LstStarter.remove(Starter)
        return


def ModifyStarter(self, id, name=None, ingredients=None, price=None):
    """
    Cette fonction permet de modifier une entrée du menu.
    """
    for Starter in self.LstStarter:
        if Starter.id == id:
            if name:
                Starter.name = name
            if ingredients:
                Starter.ingredients = ingredients
            if price:
                Starter.price = price
            return


def ReadStarter(self, id, name, ingredients, price):
    """
    Cette fonction permet de lire une entrée du menu.
    """
    for Starter in self.LstStarter:
        if Starter.id == id:
            print(f"Name: {Starter.name}, Ingredients: {Starter.ingredients}, Price: {Starter.price}")
        return