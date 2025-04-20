from Drinks import Drinks

def AddDrink(self, id, name, ingredients, price):
    """
    Cette fonction permet d'ajouter une boisson au menu.
    """
    Drink = Drink(self, id, name, ingredients, price)
    self.LstDrink.append(Drink)
    return


def RemoveDrink(self, id):
    """
    Cette fonction permet de supprimer une boisson du menu.
    """
    for Drink in self.LstDrink:
        if Drink.id == id:
            self.LstDrink.remove(Drink)
        return


def ModifyDrink(self, id, name=None, ingredients=None, price=None):
    """
    Cette fonction permet de modifier une boisson du menu.
    """
    for Drink in self.LstDrink:
        if Drink.id == id:
            if name:
                Drink.name = name
            if ingredients:
                Drink.ingredients = ingredients
            if price:
                Drink.price = price
            return


def ReadDrink(self, id, name, ingredients, price):
    """
    Cette fonction permet de lire une boisson du menu.
    """
    for Drink in self.LstDrink:
        if Drink.id == id:
            print(f"Name: {Drink.name}, Ingredients: {Drink.ingredients}, Price: {Drink.price}")
        return