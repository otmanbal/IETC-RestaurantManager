<<<<<<< HEAD
from models.Table import Table

table_list = []

def addTable(number, capacity):
    """
        Creation d'une nouvelle table
    """
    table = Table(number, capacity) 
    table_list.append(table)             
    return table

    

def displayInfo(self):
    """
        Afficher les informations de la table
    """
    #print("la valeur is free est: ", self.is_free)

    if self.is_free:
        status = "Libre"
    else:
        status = "Occupée"

    print(f"Table {self.number} - Capacité: {self.capacity} - Statut: {status}")
    


def showTables():
    """
        Afficher toutes les tables
    """
    for table in table_list:
        displayInfo(table) 


def updateTableStatus(number, is_free):
    """
        Modification de l'état (libre/occupée) d'une table si le
        numéro correspond on effectue une modification de l'état
    """
    for table in table_list:
        if table.number == number:
            table.is_free = is_free
            return table
    return None


def deleteTable(number):
    """
        on parcourt une copie de la liste (table_list[:]) pour
        Supprimer une table selon son numéro et
        garde toutes les tables sauf celle à supprimer
    """
    global table_list
    for table_del in table_list[:]:
        if table_del.number == number:
            table_list.remove(table_del)


def busy(self):
    """
        Cette méthode permet de changer l'état de la table à "occupée"
    """
    self.is_free = False
    return self.is_free

    
def free(self):
    """
        Cette methode remet la table à l'etat "libre"
    """
    self.is_free = True
    return self.is_free
=======
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
>>>>>>> dev
