import sys
from PySide6.QtWidgets import QApplication
from views.mainWindow import mainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)

    main_window = mainWindow()
    main_window.show()
    
    sys.exit(app.exec())