# controllers/table_controller.py
from models import persist                 # <- models/persist.py
from models.order import TableState
from models.menu import CARTE              # <- dict ou objet carte

from views.main_view import MainView   # <- vue principale
from views.tables_view import TableView # <- popup commande

# config fixe : table_id -> seats
TABLE_CONFIG = {1: 8, 2: 4, 3: 4, 4: 2, 5: 4, 6: 4, 7: 2, 8: 6, 9: 2}

class TableController:
    def __init__(self):
        self.states = persist.load_states()          # {id: TableState}
        self.main   = MainView(self, TABLE_CONFIG) # on passe la config
        self.main.show_tables(self.states)

    # ---------- callback vue -------------------------------------------
    def on_table_clicked(self, table_id: int):
        state = self.states.get(table_id)
        dlg   = TableView(menu=CARTE,
                            previous=(state.order if state else None),
                            parent=self.main)

        if dlg.exec():                # utilisateur a validé
            seats = state.seats if state else TABLE_CONFIG[table_id]
            if dlg.is_free():
                new_state = TableState(table_id, seats, "free", None)
            else:
                new_state = TableState(table_id, seats, "occupied", dlg.order())
            self.states[table_id] = new_state
            persist.save_state(new_state)
            self.main.update_button(new_state)
