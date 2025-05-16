from Menu import Menu

class Dessert(Menu):
    """
    C'est une classe enfant (Dessert) qui hérite de la classe parent (Menu).
    Elle est utilisée pour créer des objets de type Dessert.
    """
    def __init__(self, id, name, ingredients, price):
        super().__init__(id, name, ingredients, price)