from model.reservation_model import ReservationModel
from view.finance_view import FinanceView

class FinanceController:
    def __init__(self, view: FinanceView):
        self.view = view
        self.model = ReservationModel()

    def load_and_display_data(self, json_path):
        """
        Charge les réservations depuis le fichier JSON et met à jour la vue :
        - Affiche les paiements (tableau du haut)
        - Affiche les totaux journaliers (tableau du bas)
        """
        # Charger les réservations via le modèle
        reservations = self.model.load_reservations(json_path)

        # Mettre à jour la vue avec les paiements
        self.view.populate_payments(reservations)

        # Calculer et afficher les totaux journaliers
        daily_totals = self.model.compute_daily_totals(reservations)
        self.view.populate_daily_totals(daily_totals)
