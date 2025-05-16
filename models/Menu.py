<<<<<<< HEAD
from dataclasses import dataclass

@dataclass
class MenuItem:
    name: str
    price: float

    def __str__(self) -> str:          # affichage lisible
        return f"{self.name} – {self.price:.2f} €"


class Entree(MenuItem):   pass
class Plat(MenuItem):     pass
class Dessert(MenuItem):  pass


# entrées
CARTE_ENTREES = [
    Entree("Accra de morue (beignets de poisson)",6.00),
    Entree("Salade de papaye verte",5.50),

    Entree("Briouates au fromage",6.20),
    Entree("Zaalouk (caviar d’aubergine)",5.80),

    Entree("Taboulé libanais",6.00),
    Entree("Houmous traditionnel",5.50),
]

# plats
CARTE_PLATS = [
    Plat("Poulet DG (Directeur Général)",17.50),
    Plat("Ndolé crevettes & arachides",18.00),

    Plat("Tajine d’agneau aux pruneaux",18.50),
    Plat("Couscous royal",17.90),

    Plat("Chiche taouk (brochettes de poulet)",16.50),
    Plat("Kefta de boeuf grillée",15.00),
]

# desserts
CARTE_DESSERTS = [
    Dessert("Beignets banane",4.20),
    Dessert("Puff‑puff & sirop",4.00),

    Dessert("Chebakia au miel",4.50),
    Dessert("Pastilla au lait",4.80),

    Dessert("Baklava pistache",4.20),
    Dessert("Mouhalabieh (flan au lait parfumé)",4.00),
]
=======
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
        self.LstMenu = []
>>>>>>> dev
