import display
import random

animals = [1, 2, 3, 4]
ecosystem = [[2, 1], [2, 1]]
"""ecosystem = [
    [1, 1, 1, 1, 4, 4, 4, 2, 2, 3],
    [3, 3, 3, 3, 4, 4, 4, 2, 2, 3],
    [2, 2, 2, 2, 4, 4, 4, 2, 2, 3],
    [1, 2, 3, 3, 4, 4, 4, 2, 2, 3],
    [1, 2, 3, 3, 4, 4, 4, 2, 2, 3],
    [1, 1, 1, 1, 4, 4, 4, 2, 2, 3],
    [3, 3, 3, 3, 4, 4, 4, 2, 2, 3],
    [2, 2, 2, 2, 4, 4, 4, 2, 2, 3],
    [1, 2, 3, 3, 4, 4, 4, 2, 2, 3],
    [1, 2, 3, 3, 4, 4, 4, 2, 2, 3],
]"""


def change_animal(micro_ecosystem):
    # Détermine la proie et le prédateur
    prey = micro_ecosystem[1][1]
    # On déplace l'index dans le tableau animals pour déterminer le prédateur
    predator = animals[prey - 2]

    # Je reprends mon écosystème et je me débarasse de l'animal central pour récupérer les autres animaux autour
    others_animals = [micro_ecosystem[0], [micro_ecosystem[1][0], micro_ecosystem[1][2]], micro_ecosystem[2]]
    # J'initialise le nombre d'animaux au sein d'un dictionnaire ...
    count_animals = {key: 0 for key in animals}

    # ... et j'en fais le décompte
    for line in others_animals:
        for entity in line:
            count_animals[entity] += 1

    # Je détermine les animaux étant les plus nombreux
    max_value = max(count_animals.values())

    # Je détermine s'il y a un ou plusieurs animaux dominants
    dominant_animal = []
    for key, value in count_animals.items():
        if value == max_value:
            dominant_animal.append(key)

    # Si les prédateurs sont en majorité, je change la proie en prédateur
    if len(dominant_animal) == 1 and dominant_animal[0] == predator:
        micro_ecosystem[1][1] = predator
    elif len(dominant_animal) == 2:
        # S'il y a autant de proies que de prédateurs, on a 50% de chance de changer l'animal
        if (dominant_animal[0] or dominant_animal[1] == predator) and (
                dominant_animal[0] or dominant_animal[1] == prey):
            if random.randint(0, 1) == 0:
                micro_ecosystem[1][1] = predator
        # S'il y autant de prédateurs que d'animaux neutres, la proie est remplacée
        else:
            micro_ecosystem[1][1] = predator
    return micro_ecosystem


# Fonction qui parcourt un nouvel écosystème et met à jour tous ses animaux
def update_ecosystem(ecosystem):
    new_macro_ecosystem = [[0 for x in range(len(ecosystem))] for x in range(len(ecosystem))]
    for line in range(len(ecosystem)):
        for column in range(len(ecosystem[line])):
            new_macro_ecosystem[line][column] = ecosystem[line][column]

    # On génère un micro-écosystème pour chaque case, constituée de celle-ci et des 8 cases autour
    for x in range(len(ecosystem)):
        for y in range(len(ecosystem[x])):
            # Cas normal
            if x < len(ecosystem) - 1 and y < len(ecosystem[x]) - 1:
                micro_ecosystem = [
                    [ecosystem[x - 1][y - 1], ecosystem[x - 1][y], ecosystem[x - 1][y + 1]],
                    [ecosystem[x][y - 1], ecosystem[x][y], ecosystem[x][y + 1]],
                    [ecosystem[x + 1][y - 1], ecosystem[x + 1][y], ecosystem[x + 1][y + 1]],
                ]
            # Si la case choisie est sur la dernière ligne, on prend des cases de la première ligne
            elif x == len(ecosystem) - 1 and y < len(ecosystem[x]) - 1:
                micro_ecosystem = [
                    [ecosystem[x - 1][y - 1], ecosystem[x - 1][y], ecosystem[x - 1][y + 1]],
                    [ecosystem[x][y - 1], ecosystem[x][y], ecosystem[x][y + 1]],
                    [ecosystem[0][y - 1], ecosystem[0][y], ecosystem[0][y + 1]],
                ]
            # Si la case choisie est sur la dernière colonne, on prend des cases de la première colonne
            elif x < len(ecosystem) - 1 and y == len(ecosystem[x]) - 1:
                micro_ecosystem = [
                    [ecosystem[x - 1][y - 1], ecosystem[x - 1][y], ecosystem[x - 1][0]],
                    [ecosystem[x][y - 1], ecosystem[x][y], ecosystem[x][0]],
                    [ecosystem[x + 1][y - 1], ecosystem[x + 1][y], ecosystem[x + 1][0]],
                ]
            # Si la case choisie est sur la dernière ligne et la première colonne, on prend des cases de la première ligne et de la première colonne
            else:
                micro_ecosystem = [
                    [ecosystem[x - 1][y - 1], ecosystem[x - 1][y], ecosystem[x - 1][0]],
                    [ecosystem[x][y - 1], ecosystem[x][y], ecosystem[x][0]],
                    [ecosystem[0][y - 1], ecosystem[0][y], ecosystem[0][0]],
                ]
            new_animal = change_animal(micro_ecosystem)[1][1]
            new_macro_ecosystem[x][y] = new_animal

    return new_macro_ecosystem


# update_ecosystem(ecosystem)
display.display_ecosystem(ecosystem, update_ecosystem, 100)
