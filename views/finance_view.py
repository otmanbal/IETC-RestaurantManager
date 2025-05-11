from PySide6.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem, QLabel, QHeaderView
from PySide6.QtCore import Qt
from collections import defaultdict
from datetime import datetime

class FinanceView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance View")

        layout = QVBoxLayout(self)

        # Tableau du haut : paiements
        self.payment_table = QTableWidget()
        self.payment_table.setColumnCount(5)
        self.payment_table.setHorizontalHeaderLabels(["ID", "Table No.", "Date", "Payment Type", "Price"])
        self.payment_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.payment_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        # Tableau du bas : totaux journaliers
        self.daily_total_table = QTableWidget()
        self.daily_total_table.setColumnCount(3)
        self.daily_total_table.setHorizontalHeaderLabels(["ID", "Date", "Daily Total"])
        self.daily_total_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.daily_total_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        layout.addWidget(QLabel("Payment Records"))
        layout.addWidget(self.payment_table)
        layout.addWidget(QLabel("Daily Totals"))
        layout.addWidget(self.daily_total_table)

        self.setLayout(layout)


        def populate_payments(self, payment_list):
        self.payment_table.setRowCount(0)
        for record in payment_list:
            row = self.payment_table.rowCount()
            self.payment_table.insertRow(row)
            self.payment_table.setItem(row, 0, QTableWidgetItem(str(record["id"])))
            self.payment_table.setItem(row, 1, QTableWidgetItem(str(record["table_no"])))
            self.payment_table.setItem(row, 2, QTableWidgetItem(record["date"]))
            self.payment_table.setItem(row, 3, QTableWidgetItem(record["payment_type"]))
            self.payment_table.setItem(row, 4, QTableWidgetItem(f"{record['price']:.2f}"))