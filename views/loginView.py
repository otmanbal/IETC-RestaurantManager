import json
import os
from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox
)
from PySide6.QtCore import Signal, Qt

class LoginPage(QWidget):
    login_successful = Signal(str)  # Signal avec le nom d'utilisateur

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connexion - Restaurant Manager")
        self.setFixedSize(300, 200)
        self.utilisateurs = self.load_users()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label_info = QLabel("Veuillez vous connecter")
        self.label_info.setAlignment(Qt.AlignCenter)

        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Nom d'utilisateur")

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Mot de passe")
        self.input_password.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton("Se connecter")
        self.btn_login.clicked.connect(self.check_credentials)

        layout.addWidget(self.label_info)
        layout.addWidget(self.input_username)
        layout.addWidget(self.input_password)
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

    def load_users(self):
        
        with open("employes.json", 'r') as f:
            print("ca marche bstahek")
            return print(json.load(f))

    def check_credentials(self):
        username = self.input_username.text()
        password = self.input_password.text()

        # Recherche dans admins + users
        for user in self.utilisateurs.get("admins", []) + self.utilisateurs.get("users", []):
            if user["nom"] == username and user["mot_de_passe"] == password:
                self.login_successful.emit(username)
                return

        QMessageBox.warning(self, "Erreur", "Nom d'utilisateur ou mot de passe incorrect.")
