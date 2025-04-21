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
