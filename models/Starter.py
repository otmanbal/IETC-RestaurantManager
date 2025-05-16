from Menu import Menu

class Starter(Menu):
    """
    C'est une classe enfant (Entrée) qui hérite de la classe parent (Menu).
    Elle est utilisée pour créer des objets de type Entrée.
    """
    def __init__(self, id, name, ingredients, price):
        super().__init__(id, name, ingredients, price)