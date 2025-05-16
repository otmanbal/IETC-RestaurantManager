import sys
from PySide6.QtWidgets import QApplication
from views.finance_view import FinanceView
from controllers.finance_controller import FinanceController
from views.mainWindow import mainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)

    view = FinanceView()
    controller = FinanceController(view)
    controller.load_and_display_data("database/reservation.json")
    view.setWindowTitle("Restaurant Manager")
    view.resize(1000, 600)
    view.show()
    sys.exit(app.exec())
    main_window = mainWindow()
    main_window.show()
    
    sys.exit(app.exec())