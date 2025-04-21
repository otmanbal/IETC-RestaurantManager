class Client:

    
    def __init__(self, client_id, name, group_size):
        """
            Constructeur de la classe Client pour initialiser
            Chaque client qui aura un ID unique le nom, 
            le nombre de personnes et la table assignée 
            initialisée à None (aucune table attribuée au départ).
        """
        self.client_id = client_id       
        self.name = name
        self.group_size = group_size
        self.assigned_table = None
