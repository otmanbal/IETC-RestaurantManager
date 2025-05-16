from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QStackedWidget,
    QWidget, QSizePolicy, QPushButton, QVBoxLayout
)
from PySide6.QtGui import QPixmap, QIcon, QAction
from PySide6.QtCore import QSize

from views.tablesView import TablesView
from views.menuView import MenuView
from views.financeView import FinanceView
from views.profileView import ProfileView
from models.order import TableState

class MainWindow(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.setWindowTitle("Restaurant Manager")
        self.resize(800, 600)
        self.controller = controller

        # Toolbar de navigation
        toolbar = QToolBar("Navigation")
        self.addToolBar(toolbar)

        # Zone centrale avec les pages
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Pages
        self.page_tables = TablesView()
        self.page_menu = MenuView()
        self.page_finance = FinanceView()
        self.page_profil = ProfileView()

        self.stack.addWidget(self.page_tables)   # index 0
        self.stack.addWidget(self.page_menu)     # index 1
        self.stack.addWidget(self.page_finance)  # index 2
        self.stack.addWidget(self.page_profil)   # index 3

        # Création des boutons de navigation
        self.add_toolbar_action(toolbar, "Tables", 0)
        self.add_toolbar_action(toolbar, "Menu", 1)
        self.add_toolbar_action(toolbar, "Finance", 2)

        # Espacement pour icône de profil à droite
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        toolbar.addWidget(spacer)

        # Icône de profil à droite
        profile_pixmap = QPixmap("ressources/images/pdp.webp")
        profile_icon = QIcon(profile_pixmap.scaled(40, 40))
        action_profil = QAction(profile_icon, "", self)
        action_profil.setToolTip("Profil")
        action_profil.triggered.connect(lambda: self.stack.setCurrentIndex(3))
        toolbar.addAction(action_profil)
        toolbar.setIconSize(QSize(40, 40))

        # Optionnel : pour affichage dynamique des tables si un contrôleur est fourni
        if self.controller:
            self.init_tables()

    def add_toolbar_action(self, toolbar, name, index):
        action = QAction(name, self)
        action.triggered.connect(lambda: self.stack.setCurrentIndex(index))
        toolbar.addAction(action)

    # Pour créer des boutons dynamiques de tables si besoin
    def init_tables(self):
        layout = QVBoxLayout()
        self.page_tables.setLayout(layout)
        self.buttons = {}
        for table_id in range(1, 6):  # Exemple : 5 tables
            btn = QPushButton(f"Table {table_id}")
            btn.clicked.connect(lambda checked, tid=table_id: self._on_btn_click(tid))
            layout.addWidget(btn)
            self.buttons[table_id] = btn

    def show_tables(self, states: dict[int, TableState]):
        for tid, state in states.items():
            self.update_button(state)

    def update_button(self, state: TableState):
        btn = self.buttons[state.table_id]
        if state.status == "occupied":
            btn.setStyleSheet("background:red;")
            btn.setText(f"Table {state.seats}\nTotal {state.order.total:.2f} €")
        else:
            btn.setStyleSheet("background:green;")
            btn.setText(f"Table {state.seats}")

    def _on_btn_click(self, table_id: int):
        if self.controller:
            self.controller.on_table_clicked(table_id)