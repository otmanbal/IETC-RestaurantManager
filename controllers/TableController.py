from views.table_dialog import TableDialog
from models.persist import get_last_order, add_order, close_table

class TableController:
    def __init__(self, main_window):
        self.main_window = main_window

    def handle_table_click(self, table_id: int, label: str):
        previous_order = get_last_order(table_id)
        dialog = TableDialog(label, previous_order=previous_order, parent=self.main_window)
        if dialog.exec():
            btn = self.main_window.buttons[table_id]
            if dialog.occupied:
                add_order(table_id, dialog.order)
                total = sum(item["price"] * item["qty"] for cat in dialog.order.values() for item in cat)
                btn.setStyleSheet("background-color: red;")
                btn.setText(f"{label}\nTotal : {total:.2f} €")
            else:
                close_table(table_id)
                btn.setStyleSheet("background-color: green;")
                btn.setText(label)
