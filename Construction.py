class Construction:
    def __init__(self, id, description, valeur, unite, date):
        self.id = id
        self.description = description
        self.valeur = valeur
        self.unite = unite
        self.date = date

    def detail(self):
        print('description ', self.description)
        print('valeur ', self.valeur)
        print('unite ', self.unite)
        print('date ', self.date)
    
