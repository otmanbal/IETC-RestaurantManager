import sys
from PySide6.QtWidgets import QApplication
from views.test import FenetrePrincipale
from views.loginView import LoginPage

if __name__ == "__main__":


    app = QApplication(sys.argv)

    main_window = FenetrePrincipale()
    main_window.show()
    
    

    sys.exit(app.exec())