from controllers.ClientController import *
from controllers.TableController import *

# Création des tables

addTable(1, 2)
addTable(2, 2)
addTable(3, 6)
addTable(4, 4)

# Affichage initial des tables
print("\n--- Tables disponibles ---")
showTables()

# Création de clients
client1 = addClient("Alice", 2)
client2 = addClient("Mickbron", 3)

# Affichage des clients
print("\n--- Clients ---")
showClients()

# Assigner une table au client Alice
assignTableClient(client1.client_id, 1)
# Affichage après assignation
print("\n--- Après assignation ---")
showTables()
showClients()

# Le client Alice quitte la table
leaveTable(client1)

# Affichage après libération
print("\n--- Après libération ---")
showTables()
showClients()

# Suppression d'une table et d'un client
deleteTable(2)
deleteClient(client2.client_id)

# Affichage final
print("\n--- Après suppression ---")
showTables()
showClients()
