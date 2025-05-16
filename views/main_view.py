from typing import Dict
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt

from models.order import TableState
from models.menu import TABLE_SIZE_MAP

# views/main_window.py
class MainView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        ...  # mise en place des boutons

    def show_tables(self, states: dict[int, TableState]):
        for tid, state in states.items():
            self.update_button(state)

    def update_button(self, state: TableState):
        btn = self.buttons[state.table_id]
        if state.status == "occupied":
            btn.setStyleSheet("background:red;")
            btn.setText(f"Table {state.seats}\nTotal {state.order.total:.2f} €")
        else:
            btn.setStyleSheet("background:green;")
            btn.setText(f"Table {state.seats}")

    # slot connecté au clic d'un bouton
    def _on_btn_click(self, table_id: int):
        self.controller.on_table_clicked(table_id)
