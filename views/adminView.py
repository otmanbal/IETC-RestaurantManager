from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox, QDialog,
    QFormLayout, QLineEdit, QDialogButtonBox
)
import json
import os

# Chemin vers le fichier JSON (si$mulé ici)
DATA_FILE = "employes.json"

# Exemple de données si le fichier n'existe pas
EMPLOYES_EXEMPLE = [
    {"id": 1, "nom": "Alice Dupont", "poste": "Serveuse", "statut": "Actif"},
    {"id": 2, "nom": "Jean Martin", "poste": "Cuisinier", "statut": "Inactif"}
]

class EmployeeDialog(QDialog):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)
        self.setWindowTitle("Détails Employé")
        self.layout = QFormLayout(self)

        self.nom = QLineEdit()
        self.poste = QLineEdit()
        self.id = QLineEdit()
        self.statut = QLineEdit()

        if data:
            self.nom.setText(data["nom"])
            self.poste.setText(data["poste"])
            self.id.setText(str(data["id"]))
            self.statut.setText(data["statut"])

        self.layout.addRow("Nom:", self.nom)
        self.layout.addRow("Poste:", self.poste)
        self.layout.addRow("ID:", self.id)
        self.layout.addRow("Statut:", self.statut)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def get_data(self):
        return {
            "nom": self.nom.text(),
            "poste": self.poste.text(),
            "id": int(self.id.text()),
            "statut": self.statut.text()
        }

class AdminView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion des Employés")
        self.layout = QVBoxLayout(self)
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        # Boutons
        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("Ajouter Employé")
        self.edit_btn = QPushButton("Modifier")
        self.del_btn = QPushButton("Supprimer")
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.del_btn)
        self.layout.addLayout(btn_layout)

        # Connexions
        self.add_btn.clicked.connect(self.add_employee)
        self.edit_btn.clicked.connect(self.edit_employee)
        self.del_btn.clicked.connect(self.delete_employee)

        self.load_data()

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'w') as f:
                json.dump(EMPLOYES_EXEMPLE, f, indent=2)

        with open(DATA_FILE, 'r') as f:
            self.employes = json.load(f)

        self.refresh_table()

    def refresh_table(self):
        self.table.clear()
        self.table.setRowCount(len(self.employes))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Nom", "Poste", "ID", "Statut"])

        for row, emp in enumerate(self.employes):
            self.table.setItem(row, 0, QTableWidgetItem(emp["nom"]))
            self.table.setItem(row, 1, QTableWidgetItem(emp["poste"]))
            self.table.setItem(row, 2, QTableWidgetItem(str(emp["id"])))
            self.table.setItem(row, 3, QTableWidgetItem(emp["statut"]))

    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.employes, f, indent=2)

    def add_employee(self):
        dialog = EmployeeDialog(self)
        if dialog.exec():
            self.employes.append(dialog.get_data())
            self.save_data()
            self.refresh_table()

    def edit_employee(self):
        row = self.table.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un employé.")
            return
        data = self.employes[row]
        dialog = EmployeeDialog(self, data)
        if dialog.exec():
            self.employes[row] = dialog.get_data()
            self.save_data()
            self.refresh_table()

    def delete_employee(self):
        row = self.table.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un employé.")
            return
        confirm = QMessageBox.question(
            self, "Supprimer", "Confirmer la suppression de l'employé ?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            del self.employes[row]
            self.save_data()
            self.refresh_table()
