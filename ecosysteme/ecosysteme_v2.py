# La case centrale représente la proie et devra être modifiée en fonction du nombre de prédateurs autour.
# S’il y a plus de prédateurs alors la proie sera remplacée.
# Si au contraire ils sont en minorité alors il n’y a pas de changement.
# S’il y a en majorité à la fois des prédateurs et des proies alors il y a une chance sur deux que la proie soit remplacée par le prédateur.
# S’il y a en majorité à la fois les prédateurs et des animaux neutres, alors la proie est remplacée par le prédateur.
import random
from random import choice

ANIMAUX = [1, 2, 3]


def afficher_matrice(matrice):
    for ligne in matrice:
        print(" ".join(map(str, ligne)))


def calculer_voisins(matrice, i, j):
    animal_central = matrice[i][j]
    min_row, max_row = i - 1, i + 2
    min_col, max_col = j - 1, j + 2
    voisins_proies = 0
    voisins_predateurs = 0
    voisins_neutres = 0

    for x in range(min_row, max_row):
        for y in range(min_col, max_col):
            if x != i or y != j:
                if matrice[x][y] == (animal_central + 1) % 3:
                    voisins_proies += 1
                elif matrice[x][y] == (animal_central - 1) % 3:
                    voisins_predateurs += 1
                elif matrice[x][y] == animal_central:
                    voisins_neutres += 1

    return voisins_proies, voisins_predateurs, voisins_neutres


def evolution_ecosysteme(matrice):
    nouvelle_matrice = [ligne.copy() for ligne in matrice]

    for i in range(1, len(matrice) - 1):
        for j in range(1, len(matrice[i]) - 1):
            voisins_proies, voisins_predateurs, voisins_neutres = calculer_voisins(matrice, i, j)

            if voisins_predateurs > voisins_proies:
                nouvelle_matrice[i][j] = (matrice[i][j] - 1) % 3
            elif voisins_predateurs < voisins_proies:
                pass
            elif voisins_predateurs == voisins_proies and random.choice([True, False]):
                nouvelle_matrice[i][j] = (matrice[i][j] - 1) % 3
            elif voisins_predateurs + voisins_neutres > voisins_proies:
                nouvelle_matrice[i][j] = (matrice[i][j] - 1) % 3

    return nouvelle_matrice


def mettre_a_jour_ecosysteme(ecosysteme):
    ecosysteme_evolution = evolution_ecosysteme(ecosysteme)
    return ecosysteme_evolution


# Exemple d'utilisation avec une grille de 5x5
N = 5
ecosysteme_initial = [[choice(ANIMAUX) for _ in range(N)] for _ in range(N)]

print("---------- Avant ----------")
afficher_matrice(ecosysteme_initial)

ecosysteme_mis_a_jour = mettre_a_jour_ecosysteme(ecosysteme_initial)

print("\n---------- Après ----------")
for i in range(100):
    afficher_matrice(ecosysteme_mis_a_jour)
    print("\n---------- Après ----------")

