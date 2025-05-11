from PySide6.QtWidgets import QMainWindow, QTabWidget
from finance_view import FinanceView
from controller.finance_controller import FinanceController

class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restaurant Manager")
        self.resize(1000, 600)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Ajouter l'onglet Finance
        finance_view = FinanceView()
        finance_controller = FinanceController(finance_view)
        finance_controller.load_and_display_data("data/reservations.json")

        self.tabs.addTab(finance_view, "Finance")
