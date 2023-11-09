from modele.Robot import Robot


class RobotMobile(Robot):

    def __init__(self, robot_type=Robot.DEFAULT_ROBOT_TYPE, abs=0, ord=0):
        super().__init__(robot_type)
        self._abscisse = abs
        self._ordonnee = ord

    @property
    def abscisse(self):
        return self._abscisse

    @property
    def ordonnee(self):
        return self._ordonnee

    def afficher_position(self):
        return "Position : [abs=%d ; ord=%d]" % (self._abscisse, self._ordonnee)

    def avancer(self, nombre_metres):
        if self.orientation == "EST":
            self._abscisse += nombre_metres
        elif self.orientation == "OUEST":
            self._abscisse -= nombre_metres
        elif self.orientation == "NORD":
            self._ordonnee += nombre_metres
        elif self.orientation == "SUD":
            self._ordonnee -= nombre_metres

    def __str__(self):
        return super().__str__() + "\n" + self.afficher_position() + "\n"

