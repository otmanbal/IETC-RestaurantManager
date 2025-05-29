from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton
)
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl

class OrdersByDateView(QWidget):
    def __init__(self, date):
        super().__init__()
        self.setWindowTitle(f"Commandes du {date}")
        self.resize(600, 400)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(f"Commandes du {date}"))
