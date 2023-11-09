# Définition de la fonction pour calculer les grains de riz sur l'échiquier
def calculer_grains_riz():
    # Définition du nombre de lignes et de colonnes de l'échiquier
    lignes, colonnes = 8, 8
    # Initialisation du total des grains de riz
    total_grains = 0
    # Création d'un échiquier vide (liste bidimensionnelle)
    echiquier = [[0] * colonnes for _ in range(lignes)]

    # Convertir les indices de colonnes en lettres majuscules
    lettres_colonnes = [chr(ord('A') + i) for i in range(colonnes)]

    # Boucle pour parcourir chaque case de l'échiquier
    for ligne in range(lignes):
        for colonne in range(colonnes):
            # Calcul du numéro de la case dans l'échiquier
            num_case = ligne * colonnes + colonne + 1
            # Formatage du numéro avec un zéro devant s'il est inférieur à 10
            num_formate = str(num_case).zfill(2)
            # Calcul du nombre de grains de riz pour cette case
            grains_riz = 2 ** (num_case - 1)
            # Assignation du nombre de grains à la case correspondante dans l'échiquier
            echiquier[ligne][colonne] = grains_riz
            # Ajout du nombre de grains au total
            total_grains += grains_riz
            # Affichage du numéro de la ligne comme lettre majuscule et de la colonne comme chiffre
            print(f"Case {num_formate} : ({lettres_colonnes[colonne]}, {ligne + 1})", end="\t")
        print("\n")  # Aller à la ligne après chaque ligne de l'échiquier

    # # Affichage du nombre de grains par case de l'échiquier
    # print("Échiquier de grains de riz (numéro de case) :")
    # for ligne in echiquier:
    #     print("\t".join(map(str, ligne)))

    # Affichage du total des grains de riz
    print("\nTotal des grains de riz sur l'échiquier :", total_grains)


# Appel de la fonction pour exécuter le calcul et l'affichage
calculer_grains_riz()
