# La case centrale représente la proie et devra être modifiée en fonction du nombre de prédateurs autour.
# S’il y a plus de prédateurs alors la proie sera remplacée.
# Si au contraire ils sont en minorité alors il n’y a pas de changement.
# S’il y a en majorité à la fois des prédateurs et des proies alors il y a une chance sur deux que la proie soit remplacée par le prédateur.
# S’il y a en majorité à la fois les prédateurs et des animaux neutres, alors la proie est remplacée par le prédateur.
import random
# import display


# def update_ecosystem():
#     pass
#
#
# ecosystem = ''
# update_ecosystem_callback = update_ecosystem()
# number_of_steps = 100
#
# display.display_ecosystem(ecosystem, update_ecosystem_callback, number_of_steps)

# Création de l'écosystème initial
# Dimensions de l'écosystème
nb_lignes = 3
nb_colonnes = 3

# Création de l'écosystème initial avec des boucles for
ecosysteme_initial = []

for i in range(nb_lignes):
    ligne = []
    for j in range(nb_colonnes):
        # Ajout d'une valeur aléatoire entre 1 et 3 avec randint()
        ligne.append(random.randint(1, 3))
    ecosysteme_initial.append(ligne)


# Affichage de la matrice en console
def afficher_matrice(matrice):
    for lign in matrice:
        print(" ".join(map(str, lign)))


def calculer_voisins(matrice, i, j):
    # Définition des types d'animaux
    animal_central = matrice[i][j]

    # Définir les bornes pour la fenêtre 3x3 autour de l'animal central
    min_row, max_row = i - 1, i + 2
    min_col, max_col = j - 1, j + 2

    # Initialiser les variables pour compter les proies, prédateurs et neutres dans la fenêtre 3x3
    voisins_proies = 0
    voisins_predateurs = 0
    voisins_neutres = 0

    # Parcourir la fenêtre 3x3 autour de l'animal central
    for x in range(min_row, max_row):
        for y in range(min_col, max_col):
            # Vérifier si la cellule voisine n'est pas l'animal central
            if x != i or y != j:
                # Vérifier si la cellule voisine contient une proie
                if matrice[x][y] == (animal_central + 1) % 3:
                    voisins_proies += 1
                elif matrice[x][y] == (animal_central - 1) % 3:
                    voisins_predateurs += 1
                elif matrice[x][y] == animal_central:
                    voisins_neutres += 1

    return voisins_proies, voisins_predateurs, voisins_neutres


# Evolution de l'écosystème
def evolution_ecosysteme(matrice):
    # Crée une nouvelle matrice pour stocker l'écosystème après l'évolution
    nouvelle_matrice = [ligne.copy() for ligne in matrice]

    # Parcours de l'écosystème en excluant les bords
    for i in range(1, len(matrice) - 1):
        for j in range(1, len(matrice[i]) - 1):
            # Calculer les voisins
            voisins_proies, voisins_predateurs, voisins_neutres = calculer_voisins(matrice, i, j)

            # Application des règles
            # Remplacer la proie par le prédateur
            if voisins_predateurs > voisins_proies:
                nouvelle_matrice[i][j] = (matrice[i][j] - 1) % 3

            # Aucun changement si les prédateurs sont en minorité
            elif voisins_predateurs < voisins_proies:
                pass
            # Remplacer la proie par le prédateur (une chance sur deux)
            elif voisins_predateurs == voisins_proies and random.choice([True, False]):
                nouvelle_matrice[i][j] = (matrice[i][j] - 1) % 3
            # Remplacer la proie par le prédateur
            elif (voisins_predateurs + voisins_neutres > voisins_proies):
                nouvelle_matrice[i][j] = (matrice[i][j] - 1) % 3

    return nouvelle_matrice


# Affichage de l'écosystème initial
print("---------- Avant ----------")
afficher_matrice(ecosysteme_initial)

# Évolution de l'écosystème
ecosysteme_evolution = evolution_ecosysteme(ecosysteme_initial)

# Affichage de l'écosystème après évolution
print("\n---------- Après ----------")
afficher_matrice(ecosysteme_evolution)
