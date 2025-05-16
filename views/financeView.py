from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
    QHeaderView, QAbstractScrollArea, QScrollArea
)

class FinanceView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Finance View")

        # Layout principal vertical
        layout = QVBoxLayout(self)

        # Création du tableau du haut : paiements
        self.payment_table = QTableWidget()
        self.payment_table.setColumnCount(5)
        self.payment_table.setHorizontalHeaderLabels(["ID", "Table No.", "Date", "Payment Type", "Price"])
        self.payment_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.payment_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        # ScrollArea pour limiter la hauteur à 10 lignes
        payment_scroll = QScrollArea()
        payment_scroll.setWidgetResizable(True)
        payment_scroll.setWidget(self.payment_table)
        row_height = self.payment_table.verticalHeader().defaultSectionSize()
        header_height = self.payment_table.horizontalHeader().height()
        payment_scroll.setFixedHeight(row_height * 10 + header_height + 10)

        # Tableau du bas : totaux journaliers
        self.daily_total_table = QTableWidget()
        self.daily_total_table.setColumnCount(3)
        self.daily_total_table.setHorizontalHeaderLabels(["ID", "Date", "Daily Total"])
        self.daily_total_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.daily_total_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        # Ajout au layout
        layout.addWidget(QLabel("Payment Records"))
        layout.addWidget(payment_scroll)

        layout.addWidget(QLabel("Daily Totals"))
        layout.addWidget(self.daily_total_table)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Vue des finances"))

        self.setLayout(layout)

    def populate_payments(self, payment_list):
        """Remplit le tableau de paiements avec les données."""
        self.payment_table.setRowCount(0)
        for record in payment_list:
            row = self.payment_table.rowCount()
            self.payment_table.insertRow(row)
            self.payment_table.setItem(row, 0, QTableWidgetItem(str(record["id"])))
            self.payment_table.setItem(row, 1, QTableWidgetItem(str(record["table_no"])))
            self.payment_table.setItem(row, 2, QTableWidgetItem(record["date"]))
            self.payment_table.setItem(row, 3, QTableWidgetItem(record["payment_type"]))
            self.payment_table.setItem(row, 4, QTableWidgetItem(f"{record['price']:.2f}"))

    def populate_daily_totals(self, totals_list):
        """Remplit le tableau du bas avec les totaux journaliers."""
        self.daily_total_table.setRowCount(0)
        for record in totals_list:
            row = self.daily_total_table.rowCount()
            self.daily_total_table.insertRow(row)
            self.daily_total_table.setItem(row, 0, QTableWidgetItem(str(record["id"])))
            self.daily_total_table.setItem(row, 1, QTableWidgetItem(record["date"]))
            self.daily_total_table.setItem(row, 2, QTableWidgetItem(f"{record['total']:.2f}"))
