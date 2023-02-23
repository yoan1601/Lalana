class Budget:
    def __init__(self, cout, duree, volume):
        self.cout = cout
        self.duree = duree
        self.volume = volume

    def detail(self):
        print('cout ', self.cout)
        print('duree ', self.duree)
        print('volume de goudron necessaire ', self.volume)


        