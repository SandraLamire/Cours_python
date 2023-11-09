import string
import random


class Robot:
    nb_robot = 0
    valeurs_orientation_autorisees = ["NORD", "EST", "SUD", "OUEST"]
    valeurs_statut_autorisees = {1: "EN SERVICE", 2: "HORS SERVICE", 3: "EN REPARATION"}
    DEFAULT_ROBOT_TYPE = "Générique"

    def __init__(self, orientation="", statut=0, robot_type=DEFAULT_ROBOT_TYPE):
        self._robot_type = robot_type
        self._numero_serie = random.choice(string.ascii_uppercase) + random.choice(
            string.ascii_uppercase) + f"{random.randint(0, 1000000000):010d}"
        self._orientation = Robot.valeurs_orientation_autorisees[0]
        self._statut = Robot.valeurs_statut_autorisees[1]
        Robot.nb_robot += 1

    # Décorateur qui permet d'accéder à la valeur de l'attribut
    # Il change le comportement de la méthode pour en faire un getter
    @property
    def robot_type(self):
        return self._robot_type

    # Décorateur qui permet de gérer l'affectation en vérifiant la contrainte de longueur minimale
    # Il change le comportement du setter
    @robot_type.setter
    def robot_type(self, value):
        if len(value) >= 2:
            self._robot_type = type
        else:
            print("Erreur : le type d'un robot doit faire au minimum 2 caractères ou plus.")
            self._robot_type = Robot.DEFAULT_ROBOT_TYPE

    @property
    def numero_serie(self):
        return self._numero_serie

    @property
    def orientation(self):
        return self._orientation

    def modifier_orientation(self, nouvelle_orientation):
        if nouvelle_orientation in self.valeurs_orientation_autorisees:
            self._orientation = nouvelle_orientation
        else:
            print("Orientation non valide. Utilisez NORD, EST, SUD ou OUEST.")

    # Accès à la valeur textuelle de chaque clé du dictionnaire
    @property
    def statut(self):
        return self._statut

    @statut.setter
    def statut(self, nouveau_statut):
        if nouveau_statut in self.valeurs_statut_autorisees:
            self._statut = nouveau_statut
        else:
            print("Statut non valide. Utilisez 1, 2 ou 3.")

    def tourner(self, direction):
        if direction != -1 and direction != 1:
            print("Direction invalide. Le robot ne tourne pas")

        # % len permet de rester dans le range d'index
        # (ex : si robot orienté "NORD" (index 0) et tourne de 1 dans le sens horaire,
        # nouvel index = (0 + 1) % 4 = 1, ce qui correspond à "EST".
        index_orientation_courant = self.valeurs_orientation_autorisees.index(self._orientation)
        nouvel_index_orientation = (index_orientation_courant + direction) % len(self.valeurs_orientation_autorisees)
        self._orientation = self.valeurs_orientation_autorisees[nouvel_index_orientation]
        # if direction != 1 and -1:
        #     print("Le robot ne peut pas tourner dans cette direction")
        # else:
        #     taille_valeurs_orientation_autorisees = len(Robot.valeurs_orientation_autorisees)
        #     index_orientation = Robot.valeurs_orientation_autorisees.index[self._orientation + direction]
        #     self._orientation = index_orientation % taille_valeurs_orientation_autorisees

    def __str__(self):
        return "ROBOT %s - %s\nStatut : %s\nOrientation : %s" % (
            self._numero_serie, self._robot_type, self._statut, self._orientation)


'''
# EXEMPLES D'UTILISATION :
# r.robot_type("Aspirateur") ne marche pas à cause des décorateurs @property
# Il faut faire :
r = Robot("Machin chose")  # Attribution d'une valeur à travers le setter
print(r.robot_type)  # Récupération d'une valeur à travers le getter

robot = Robot(robot_type="Robot1")
print(robot.numero_serie)

robot = Robot()
print(robot.orientation)  # Accès en lecture
robot.modifier_orientation("EST")  # Modification
print(robot.orientation)  # Nouvelle valeur

robot = Robot()
print(robot.statut)  # Accès en lecture
robot._statut = 2  # Modification
print(robot.statut)  # Nouvelle valeur

print("####################################")
print(robot)
'''
