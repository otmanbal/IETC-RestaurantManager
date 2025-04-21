from models.Client import Client  
import TableController 

client_list = []
TableController.table_list

next_client_id = 1  # Pour générer un identifiant unique automatiquement


def addClient(name, group_size):
    """
        Création d'un objet Client
        et ajout a la liste des clients
    """
    global next_client_id
    new_client = Client(next_client_id, name, group_size)
    client_list.append(new_client)
    next_client_id += 1 
    return new_client



def assignTableClient(client_id, table_number):
    """
        la fonction initialise client et table à None 
        pour couvrir le cas où aucun élément ne correspond.
        Recherche un client dans la liste client_list dont
        le(client_id) correspond au numero ID du client.
        Recherche une table dans la liste tables table_list dont
        le numéro (table_number) correspond à table_number.
        si tout est valide et que la table est libre, on assigne la table au client
    """

    global table

    client = None
    for client_search in client_list:
        if client_search.client_id == client_id:
            client = client_search

    table = None
    for table_search in TableController.table_list:
        if table_search.number == table_number:
            table = table_search
    
    if client and table and table.is_free:
        assignTable(client)
        return True
    return False
    

def assignTable(self):
    """
        La méthode assignTable() permet d’assigner une table à un client.
        Elle stocke l’objet table dans l’attribut assigned_table du client,
        puis appelle la méthode busy() sur la table pour changer 
        son état à "occupée". Cela permet de gérer la disponibilité 
        des tables dans le restaurant.
    """
    self.assigned_table = table
    TableController.busy(table)



def displayInfo(self):
    """
        la méthode displayInfo() dans pour afficher 
        l’état du client et sa table assignée
    """
    
    if self.assigned_table:

        print(f"Client #{self.client_id} - {self.name} (groupe de {self.group_size}) est à la table {self.assigned_table.number}.")
    else:
        print(f"Client #{self.client_id} - {self.name} (groupe de {self.group_size}) n'a pas encore de table.")


def showClients():
    """
        Affiche les infos de chaque client
    """
    
    for client in client_list:
        displayInfo(client)



def deleteClient(client_id):
    """
        on parcourt une copie de la liste (client_list[:]) pour
        Supprimer un Client selon son numéro et
        garde tous les clients sauf celui à supprimer
    """
    global client_list
    for client_del in client_list[:]:
        if client_del.client_id == client_id:
            client_list.remove(client_del)



def leaveTable(self):
    """
        la méthode leaveTable() dans la classe pour permettre
        à un client de libérer sa table après utilisation.
        on vérifie si le client a une table assignée si c'est le cas 
        on appelle la méthode free() sur la table pour la rendre 
        à nouveau disponible et on enleve l'association entre 
        le client et la table.
    """
    global table
    if self.assigned_table:
        TableController.free(table)
        self.assigned_table = None
