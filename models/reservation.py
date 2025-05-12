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
