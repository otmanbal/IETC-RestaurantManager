class Reservation:
    def __init__(self, id, client_id, table_id, date_heure):
        """
            id : identifiant unique de la réservation (int)
            client_id : identifiant du client (int)
            table_id : identifiant de la table réservée (int)
            date_heure : date et heure de la réservation (str, format ISO recommandé)
        """
        self.id = id
        self.client_id = client_id
        self.table_id = table_id
        self.date_heure = date_heure

    def to_dict(self):
        """
            Convertit l'objet Reservation en dictionnaire pour l'enregistrement JSON.
        """
        return {
            "id": self.id,
            "client_id": self.client_id,
            "table_id": self.table_id,
            "date_heure": self.date_heure
        }

    @staticmethod
    def from_dict(data):
        """
            Crée un objet Reservation à partir d'un dictionnaire (chargé depuis JSON).
        """
        return Reservation(
            data["id"],
            data["client_id"],
            data["table_id"],
            data["date_heure"]
        )