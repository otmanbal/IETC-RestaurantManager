from PySide6.QtWidgets import (
    QMainWindow, QToolBar, QStackedWidget, QWidget,
    QSizePolicy, QMenu
)
from PySide6.QtGui import QPixmap, QIcon, QAction
from PySide6.QtCore import QSize, QPoint, QTimer

from views.tableView import TableView
from views.adminView import AdminView
from views.financeView import FinanceView
from views.loginView import LoginPage


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
        self.page_admin = AdminView()
        self.page_finance = FinanceView()

        self.stack.addWidget(self.page_tables)    # index 0
        self.stack.addWidget(self.page_admin)     # index 1
        self.stack.addWidget(self.page_finance)   # index 2

        # Actions de navigation
        action_tables = QAction("Tables", self)
        action_tables.triggered.connect(lambda: self.stack.setCurrentIndex(0))
        toolbar.addAction(action_tables)

        action_admin = QAction("Admin", self)
        action_admin.triggered.connect(lambda: self.stack.setCurrentIndex(1))
        toolbar.addAction(action_admin)

        action_finance = QAction("Finance", self)
        action_finance.triggered.connect(lambda: self.stack.setCurrentIndex(2))
        toolbar.addAction(action_finance)

        # Spacer pour pousser le profil à droite
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        toolbar.addWidget(spacer)

        # Icône de profil avec menu
        profile_pixmap = QPixmap("ressources/images/pdp.webp")
        profile_icon = QIcon(profile_pixmap.scaled(40, 40))
        action_profil = QAction(profile_icon, "", self)
        action_profil.setToolTip("Profil")
        toolbar.addAction(action_profil)
        toolbar.setIconSize(QSize(40, 40))

        # Menu contextuel pour le profil
        self.profile_menu = QMenu(self)
        self.profile_menu.addAction("Se déconnecter", self.logout)

        # Affichage du menu sur clic
        action_profil.triggered.connect(self.show_profile_menu)

    def show_profile_menu(self):
        pos = self.mapToGlobal(QPoint(self.width() - 60, 50))
        self.profile_menu.exec(pos)

    def logout(self):
        # Créer une nouvelle page de login
        self.login_page = LoginPage()
        self.login_page.login_successful.connect(self.reopen_main_window)
        self.login_page.show()

        # Fermer la fenêtre principale juste après
        QTimer.singleShot(0, self.close)

    def reopen_main_window(self, username, is_admin):
        self.login_page.close()
        new_window = mainWindow()
        new_window.show()
