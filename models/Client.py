class Client:
    def __init__(self, id, nom, telephone):
        self.id = id
        self.nom = nom
        self.telephone = telephone

    def to_dict(self):
        """
            Convertit l'objet Client en dictionnaire pour l'enregistrement JSON.
        """
        return {
            "id": self.id,
            "nom": self.nom,
            "telephone": self.telephone
        }

    @staticmethod
    def from_dict(data):
        """
            Crée un objet Client à partir d'un dictionnaire (chargé depuis JSON).
        """
        return Client(
            data["id"],
            data["nom"],
            data["telephone"]
        )