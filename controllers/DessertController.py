from Dessert import Dessert

def AddDessert(self, id, name, ingredients, price):
    """
    Cette fonction permet d'ajouter un dessert à la liste des desserts.
    """
    Dessert = Dessert(id, name, ingredients, price)
    self.LstDessert.append(Dessert)
    return


def RemoveDessert(self, id):
    """
    Cette fonction permet de supprimer un dessert de la liste des desserts.
    """
    for Dessert in self.LstDessert:
        if Dessert.id == id:
            self.LstDessert.remove(Dessert)
        return


def ModifyDessert(self, id, name=None, ingredients=None, price=None):
    """
    Cette fonction permet de modifier un dessert de la liste des desserts.
    """
    for Dessert in self.LstDessert:
        if Dessert.id == id:
            if name:
                Dessert.name = name
            if ingredients:
                Dessert.ingredients = ingredients
            if price:
                Dessert.price = price
            return


def ReadDessert(self, id, name, ingredients, price):
    """
    Cette fonction permet de lire un dessert de la liste des desserts.
    """
    for Dessert in self.LstDessert:
        if Dessert.id == id:
            print(f"Name: {Dessert.name}, Ingredients: {Dessert.ingredients}, Price: {Dessert.price}")
        return