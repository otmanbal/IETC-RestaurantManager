import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication

from controllers.TableController import TableController

def main() -> None:
    """Instancie QApplication + lance le contrôleur."""
    app = QApplication(sys.argv)
    TableController()              # crée les vues et affiche la fenêtre principale
    sys.exit(app.exec())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = FenetrePrincipale()
    window.show()

    sys.exit(app.exec())