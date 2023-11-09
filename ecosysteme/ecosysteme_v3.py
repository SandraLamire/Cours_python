# La case centrale représente la proie et devra être modifiée en fonction du nombre de prédateurs autour.

import random
from display import display_ecosystem  # Importer la fonction d'affichage
from random import choice

ANIMAUX = [1, 2, 3]


def afficher_matrice(matrice):
    """
    Affiche une matrice dans la console
    :param matrice: la matrice à afficher
    """
    for ligne in matrice:
        # Convertir les éléments de la ligne en chaînes et les joindre avec un espace
        print(" ".join(map(str, ligne)))


def calculer_voisins(matrice, i, j):
    """
    Calcule le nombre de voisins pour une cellule donnée dans la matrice
    :param matrice: la matrice représentant l'écosystème
    :param i: indice de ligne de la cellule
    :param j: indice de colonne de la cellule
    :return: un tuple avec le nombre de proies, prédateurs et neutres dans le voisinage
    """
    animal_central = matrice[i][j]  # Récupérer le type d'animal dans la cellule centrale
    voisins_proies = 0
    voisins_predateurs = 0
    voisins_neutres = 0

    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < len(matrice) and 0 <= y < len(matrice[0]) and (x != i or y != j):
                if matrice[x][y] == (animal_central + 1) % 3:
                    voisins_neutres += 1
                elif matrice[x][y] == (animal_central - 1) % 3:
                    voisins_predateurs += 1
                elif matrice[x][y] == animal_central:
                    voisins_proies += 1

    return voisins_proies, voisins_predateurs, voisins_neutres


def evolution_ecosysteme(matrice):
    """
    Met à jour l'écosystème en fonction des règles
    :param matrice: la matrice représentant l'écosystème
    :return: une nouvelle matrice représentant l'écosystème mis à jour
    """
    # Copier la matrice existante pour stocker les mises à jour
    nouvelle_matrice = [ligne.copy() for ligne in matrice]

    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            voisins_proies, voisins_predateurs, voisins_neutres = calculer_voisins(matrice, i, j)

            # S’il y a + de prédateurs = proie remplacée par son prédateur
            if voisins_predateurs > voisins_proies:
                nouvelle_matrice[i][j] = (matrice[i][j] - 1) % 3
            # S’il y a en majorité (prédateurs + proies) = une chance sur deux que proie remplacée par son prédateur.
            elif voisins_predateurs == voisins_proies and random.choice([True, False]):
                nouvelle_matrice[i][j] = (matrice[i][j] - 1) % 3
            # S’il y a en majorité (prédateurs + neutres) = proie remplacée par son prédateur.
            elif (voisins_predateurs + voisins_neutres) > voisins_proies:
                nouvelle_matrice[i][j] = (matrice[i][j] - 1) % 3
    matrice = nouvelle_matrice
    return matrice


# Exemple d'utilisation avec une grille de N par N
N = 20
ecosysteme_initial = [[choice(ANIMAUX) for _ in range(N)] for _ in range(N)]

# Affichage de l'écosystème initial
# print("---------- Avant ----------")
# afficher_matrice(ecosysteme_initial)

# Évolution de l'écosystème avec la fonction d'affichage
print("---------- Après ----------")
display_ecosystem(ecosysteme_initial, evolution_ecosysteme, number_of_steps=100)
