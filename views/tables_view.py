import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout,
    QLabel, QPushButton, QDialog, QHBoxLayout, QFrame, QCheckBox, QScrollArea, QGroupBox, QSpinBox
)
from PySide6.QtCore import Qt

from models.menu import CARTE_ENTREES, CARTE_PLATS, CARTE_DESSERTS, MenuItem

TABLE_SIZE_MAP = {2: (120, 60), 4: (120, 80), 6: (120, 200), 8: (120, 270)}
class TablesView(QDialog):
    def __init__(self, table_label: str, parent=None,previous_order=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Vue des tables"))
        self.setLayout(layout)
        self.occupied: bool | None = None
        self.order: dict[str, MenuItem | None] = {"entrée": None, "plat": None, "dessert": None}
        self.previous_order = previous_order
