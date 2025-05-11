import sys
from PySide6.QtWidgets import QApplication
from view.finance_view import FinanceView
from controller.finance_controller import FinanceController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    view = FinanceView()
    controller = FinanceController(view)
    controller.load_and_display_data("data/reservations.json")

    view.show()
    sys.exit(app.exec())
