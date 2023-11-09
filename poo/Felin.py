from Animal import Animal


class Felin(Animal):
    def __init__(self):
        super().__init__()
        print("Init Félin")

    def graou(self):
        print("Graou !")