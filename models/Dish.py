from Menu import Menu

class Dish(Menu):
    """
    C'est une classe enfant (Plat) qui hérite de la classe parent (Menu).
    Elle est utilisée pour créer des objets de type Plat.
    """
    def __init__(self, id, name, ingredients, price):
        super().__init__(id, name, ingredients, price)
        