from Animal import Animal


class Carnivore(Animal):
    def __init__(self):
        super().__init__()
        print("Init Carnivore")

    def graou(self):
        print("Scrounck ! Scrounck !")
