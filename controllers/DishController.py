from Dish import Dish

def AddDish(self, id, name, ingredients, price):
    """
    Cette fonction permet d'ajouter un plat au menu.
    """
    Dish = Dish(id, name, ingredients, price)
    self.LstDish.append(Dish)
    return


def RemoveDish(self, id):
    """
    Cette fonction permet de supprimer un plat du menu.
    """
    for Dish in self.LstDish:
        if Dish.id == id:
            self.LstDish.remove(Dish)
        return


def ModifyDish(self, id, name=None, ingredients=None, price=None):
    """
    Cette fonction permet de modifier un plat du menu.
    """
    for Dish in self.LstDish:
        if Dish.id == id:
            if name:
                Dish.name = name
            if ingredients:
                Dish.ingredients = ingredients
            if price:
                Dish.price = price
        return
    

def ReadDish(self, id, name, ingredients, price):
    """
    Cette fonction permet de lire un plat du menu.
    """
    for Dish in self.LstDish:
        if Dish.id == id:
            print(f"Name: {Dish.name}, Ingredients: {Dish.ingredients}, Price: {Dish.price}")
        return