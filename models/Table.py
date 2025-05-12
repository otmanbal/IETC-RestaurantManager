class Table:
    def __init__(self, id, capacite, disponible = True):
        """
            id : identifiant unique de la table (int)
            capacite : nombre de personnes que peut accueillir la table (int)
            disponible : booléen indiquant si la table est disponible
        """
        self.id = id
        self.capacite = capacite
        self.disponible = disponible