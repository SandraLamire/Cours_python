from poo.Carnivore import Carnivore
from poo.Felin import Felin


class Cat(Felin, Carnivore):
    # Propriété de classe
    type = "chat"

    def __init__(self, name, color):
        # Mauvaise pratique :
        # Felin.__init__(self)
        # Carnivore.__init__(self)
        # Bonne pratique :
        super().__init__()
        print("Init Cat")
        # Propriétés d'instances (non dispo sans getters/setters)
        # Attribut en private : _name, _color
        self._name = name
        self._color = color
        # Attention à ne pas confondre variables self.type, type et Cat.type qui sont toutes différentes
        # self.type
        # Cat.type

    def chasser(self):
        print(self._name, " chasse !")

    # Déclaration d'une méthode de classe
    @classmethod
    def dormir(cls):
        print(cls.type, ' dort : Zzzzz')

    # Déclaration d'une méthode static
    @staticmethod
    def miauler():
        print("Miaou !")

    # getters et setters
    def getName(self):
        return self._name

    def getColor(self):
        return self._color

    def setName(self, name):
        self._name = name

    def setColor(self, color):
        self._color = color

    def __str__(self):
        return "Nom : " + self._name + ", couleur : " + self._color


c = Cat("Tom", "gris")
print(c)
# Init Animal
# Init Carnivore
# Init Félin
# Init Cat
# Nom : Tom, couleur : gris
