class Table:

    
    def __init__(self, number, capacity):
        """
            Constructeur de la classe Table : 
            initialise le numéro, la capacite et l’etat 
            de disponibilité (libre par défaut)
        """
        self.number = number          
        self.capacity = capacity  
        self.is_free = True 
