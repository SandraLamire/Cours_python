class Intervalle:
    def __init__(self, borne_min, borne_max):
        # Vérifier et inverser les bornes si elles ne sont pas dans le bon ordre
        if borne_min > borne_max:
            borne_min, borne_max = borne_max, borne_min
        self.__borne_min = borne_min
        self.__borne_max = borne_max

    # Getters
    def get_borne_min(self):
        return self.__borne_min

    def get_borne_max(self):
        return self.__borne_max

    # Setters
    def set_borne_min(self, borne_min):
        if borne_min < self.__borne_max:
            self.__borne_min = borne_min
        else:
            print("Erreur: la borne inférieure doit être inférieure à la borne supérieure")

    def set_borne_max(self, borne_max):
        if borne_max > self.__borne_min:
            self.__borne_max = borne_max
        else:
            print("Erreur: la borne supérieure doit être supérieure à la borne inférieure")

    # retourne un nouvel Intervalle addition des deux intervalles.
    # Exemple : [2 ; 5] + [3 ; 4] = [5 ; 9]
    def __add__(self, other):
        return Intervalle(self.__borne_min + other.get_borne_min(), self.__borne_max + other.get_borne_max())

    # Retourne l’intersection des deux intervalles
    # et « None » si leur intersection est vide.
    # Exemple :  [2 ; 5]∩[3 ; 6]=[3 ; 5]
    def intersection(self, other):
        if self.__borne_max < other.get_borne_min() or other.get_borne_max() < self.__borne_min:
            return None
        else:
            return Intervalle(max(self.__borne_min, other.get_borne_min()), min(self.__borne_max, other.get_borne_max()))

    # renvoie None lorsque l’union est impossible, et le résultat autrement.
    # Exemple :  [2 ; 5] ⋃ [3 ; 6]=[2 ; 6]
    def union(self, other):
        if min(self.__borne_min, other.get_borne_min()) > max(self.__borne_max, other.get_borne_max()):
            return None
        else:
            return Intervalle(min(self.__borne_min, other.get_borne_min()), max(self.__borne_max, other.get_borne_max()))

    def __str__(self):
        return "[" + str(self.__borne_min) + " ; " + str(self.__borne_max) + "]"
