from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class TablesView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Vue des tables"))
        self.setLayout(layout)
