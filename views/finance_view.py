from PySide6.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem, QLabel, QHeaderView
from PySide6.QtCore import Qt
from collections import defaultdict
from datetime import datetime

class FinanceView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance View")