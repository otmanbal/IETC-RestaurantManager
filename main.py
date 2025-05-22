import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication

from views.financeView import FinanceView
from controllers.finance_controller import FinanceController
from views.mainWindow import mainWindow
from views.tableView import TableView





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
    
    table_view = TableView()
    table_view.show()
    
    
    sys.exit(app.exec())

