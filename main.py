import sys
from PySide6.QtWidgets import QApplication
from views.test import FenetrePrincipale

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = FenetrePrincipale()
    window.show()

    sys.exit(app.exec())