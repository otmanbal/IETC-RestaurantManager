from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class ProfileView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Bienvenue sur votre profil !")
        layout.addWidget(label)
