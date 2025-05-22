from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QLabel, QMessageBox
from models.finance_manager import add_financial_record, get_financial_summary
from models.pdf_generator import export_financial_report_pdf

class FinancesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage Finances")
        layout = QVBoxLayout()

        self.type_combo = QComboBox()
        self.type_combo.addItems(["income", "expense"])
        layout.addWidget(self.type_combo)

        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Description")
        layout.addWidget(self.description_input)

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Amount")
        layout.addWidget(self.amount_input)

        self.add_button = QPushButton("Add Record")
        self.add_button.clicked.connect(self.add_record)
        layout.addWidget(self.add_button)

        self.summary_label = QLabel()
        layout.addWidget(self.summary_label)

        self.update_summary()

        self.export_button = QPushButton("Export PDF Report")
        self.export_button.clicked.connect(self.export_pdf)
        layout.addWidget(self.export_button)

        self.setLayout(layout)

    def add_record(self):
        try:
            record_type = self.type_combo.currentText()
            description = self.description_input.text()
            amount = float(self.amount_input.text())
            add_financial_record(record_type, description, amount)
            QMessageBox.information(self, "Success", "Record added successfully.")
            self.update_summary()
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid amount.")

    def update_summary(self):
        income, expense, balance = get_financial_summary()
        self.summary_label.setText(f"Income: ${income:.2f} | Expense: ${expense:.2f} | Balance: ${balance:.2f}")

    def export_pdf(self):
        export_financial_report_pdf()
        QMessageBox.information(self, "Exported", "PDF report generated.")
