from Menu import Menu

class Drinks(Menu):
    """
    C'est une classe enfant (Boisson) qui hérite de la classe parent (Menu).
    Elle est utilisée pour créer des objets de type Boisson.
    """
    def __init__(self, id, name, ingredients, price):
        super().__init__(id, name, ingredients, price)