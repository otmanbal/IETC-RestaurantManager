from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QStackedWidget,
    QWidget, QSizePolicy
)
from PySide6.QtGui import QPixmap, QIcon, QAction
from PySide6.QtCore import QSize
from views.tablesView import TableView
from views.menuView import MenuView
from views.financeView import FinanceView
from views.profileView import ProfileView 
from views.adminView import AdminView

class mainWindow(QMainWindow):
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
        self.page_tables = TableView()
        self.page_menu = MenuView()
        self.page_finance = FinanceView()
        self.page_profil = AdminView()  # Nouvelle page profil

        self.stack.addWidget(self.page_tables)   # index 0
        self.stack.addWidget(self.page_menu)     # index 1
        self.stack.addWidget(self.page_finance)  # index 2
        self.stack.addWidget(self.page_profil)   # index 3

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

        # Spacer pour pousser l'action Profil à droite
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        toolbar.addWidget(spacer)

        # Ajout photo de profil ronde
        profile_pixmap = QPixmap("ressources/images/pdp.webp")
        profile_icon = QIcon(profile_pixmap.scaled(40, 40))

        action_profil = QAction(profile_icon, "", self)
        action_profil.setToolTip("Profil")
        action_profil.triggered.connect(lambda: self.stack.setCurrentIndex(3))
        toolbar.addAction(action_profil)
        toolbar.setIconSize(QSize(40, 40))  # Taille de l’icône

