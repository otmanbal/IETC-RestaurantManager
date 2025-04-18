from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QStackedWidget
)
from PySide6.QtGui import QAction
from views.tables_view import TablesView
from views.menu_view import MenuView
from views.finance_view import FinanceView

class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restaurant Manager")
        self.resize(800, 600)

        # Navigation
        toolbar = QToolBar("Navigation")
        self.addToolBar(toolbar)

        # Stack central
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Pages
        self.page_tables = TablesView()
        self.page_menu = MenuView()
        self.page_finance = FinanceView()

        self.stack.addWidget(self.page_tables)   # index 0
        self.stack.addWidget(self.page_menu)     # index 1
        self.stack.addWidget(self.page_finance)  # index 2

        # Actions navigation
        action_tables = QAction("Tables", self)
        action_tables.triggered.connect(lambda: self.stack.setCurrentIndex(0))
        toolbar.addAction(action_tables)

        action_menu = QAction("Menu", self)
        action_menu.triggered.connect(lambda: self.stack.setCurrentIndex(1))
        toolbar.addAction(action_menu)

        action_finance = QAction("Finance", self)
        action_finance.triggered.connect(lambda: self.stack.setCurrentIndex(2))
        toolbar.addAction(action_finance)
