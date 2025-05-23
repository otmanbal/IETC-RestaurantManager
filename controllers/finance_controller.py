from models.reservation_models import ReservationModel
from views.financeView import FinanceView

class FinanceController:
    def __init__(self, view: FinanceView):
        self.view = view
        self.model = ReservationModel()

    def load_and_display_data(self, json_path):
        reservations = self.model.load_reservations(json_path)
        self.view.populate_payments(reservations)

        daily_totals = self.model.compute_daily_totals(reservations)
        self.view.populate_daily_totals(daily_totals)
