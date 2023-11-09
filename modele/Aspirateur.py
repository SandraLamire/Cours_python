from modele.RobotMobile import RobotMobile


class Aspirateur:

    def __init__(self, marque, puissance):
        self._marque = marque
        self._puissance = puissance

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, m):
        self._marque = m

    @property
    def puissance(self):
        return self._puissance

    @puissance.setter
    def puissance(self, p):
        self._puissance = p

    def __str__(self):
        return "Aspirateur %s, puissance=%dW" % (self.marque, self.puissance)


class AspirateurRobot(RobotMobile, Aspirateur):

    def __init__(self, marque, puissance, distance):
        super().__init__()
        self._robot_type = "Aspirateur Robot"
        self._distance_max = distance
        self.puissance = puissance
        self.marque = marque
        self._abscisse = 0
        self._ordonnee = 0

    @property
    def distance_max(self):
        return self._distance_max

    @distance_max.setter
    def distance_max(self, distance):
        self._distance_max = distance

    def parcours(self):
        pass

    def __str__(self):
        return RobotMobile.__str__(self) + "Marque : %s\nPuissance : %dW" % (self.marque, self.puissance)
