class Menu:
    """
    C'est une classe parent (Menu) qui contient les méthodes de base pour le menu
    de l'application. Elle est utilisée par les classes enfants
    """
    def __init__(self, id, name, ingredients, price):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.price = price
    
