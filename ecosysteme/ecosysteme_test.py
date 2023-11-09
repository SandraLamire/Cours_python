# La case centrale représente la proie et devra être modifiée en fonction du nombre de prédateurs autour.
# S’il y a plus de prédateurs alors la proie sera remplacée.
# Si au contraire ils sont en minorité alors il n’y a pas de changement.
# S’il y a en majorité à la fois des prédateurs et des proies alors il y a une chance sur deux que la proie soit remplacée par le prédateur.
# S’il y a en majorité à la fois les prédateurs et des animaux neutres, alors la proie est remplacée par le prédateur.
import random
from display import display_ecosystem  # Importer la fonction d'affichage


def afficher_matrice(matrice):
    for ligne in matrice:
        print(" ".join(map(str, ligne)))  # Convertir les éléments de la ligne en chaînes et les joindre avec un espace


def calculer_voisins(matrice, i, j):
    animal_central = matrice[i][j]
    voisins_proies = 0
    voisins_predateurs = 0
    voisins_neutres = 0

    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < len(matrice) and 0 <= y < len(matrice[0]) and (x != i or y != j):
                if matrice[x][y] == (animal_central + 1) % 3:
                    voisins_proies += 1
                elif matrice[x][y] == (animal_central - 1) % 3:
                    voisins_predateurs += 1
                elif matrice[x][y] == animal_central:
                    voisins_neutres += 1

    return voisins_proies, voisins_predateurs, voisins_neutres



def evolution_ecosysteme(matrice):
    nouvelle_matrice = [ligne.copy() for ligne in matrice]  # Copier la matrice existante pour stocker les mises à jour

    for i in range(1, len(matrice) - 1):
        for j in range(1, len(matrice[i]) - 1 ):
            voisins_proies, voisins_predateurs, voisins_neutres = calculer_voisins(matrice, i, j)  # Calculer les voisins de la cellule

            if voisins_predateurs > voisins_proies:  # Remplacer la proie par le prédateur
                nouvelle_matrice[i][j] = (matrice[i][j] - 1) % 3
            elif voisins_predateurs < voisins_proies:  # Aucun changement si les prédateurs sont en minorité
                pass
            elif voisins_predateurs == voisins_proies and random.choice([True, False]):  # Remplacer la proie par le prédateur (une chance sur deux)
                nouvelle_matrice[i][j] = (matrice[i][j] - 1) % 3
            elif voisins_predateurs + voisins_neutres > voisins_proies:  # Remplacer la proie par le prédateur
                nouvelle_matrice[i][j] = (matrice[i][j] - 1) % 3

    return nouvelle_matrice


# Exemple d'utilisation avec une grille de N par N
N = 20
ecosysteme_initial = [[random.randint(1, 3) for _ in range(N)] for _ in range(N)]

# Affichage de l'écosystème initial
print("---------- Avant ----------")
afficher_matrice(ecosysteme_initial)

# Évolution de l'écosystème avec la fonction d'affichage
display_ecosystem(ecosysteme_initial, evolution_ecosysteme, number_of_steps=1000)
