# PALINDROME DE MOT/PHRASE :
import string

def creer_table_de_translation(phrase):
    # Créer une table de traduction pour ignorer les caractères accentués et autres
    accents = str.maketrans("àäéèëïôùüç", "aaeeeiouuc", string.punctuation + string.whitespace)
    # Convertir l'entrée en minuscules et appliquer la table de traduction
    phrase = phrase.lower().translate(accents)
    return phrase

def est_palindrome(phrase):
    # Utiliser une comparaison pour vérifier le palindrome
    return phrase == phrase[::-1]

while True:
    mot = input("Entrez un mot ou une phrase (ou 'x' pour quitter) : ")

    # Vérifiez si l'utilisateur veut quitter
    if mot.lower() == 'x':
        print("Au revoir !")
        break  # Sortez de la boucle while pour quitter le programme

    # Appliquer la table de traduction et convertir en minuscules
    mot_transforme = creer_table_de_translation(mot)

    # Supprimez les espaces du mot pour ne tenir compte que des caractères
    mot_transforme = mot_transforme.replace(" ", "")

    # Affichez le résultat
    if est_palindrome(mot_transforme):
        print("Le mot ou la phrase est un palindrome.")
    else:
        print("Le mot ou la phrase n'est pas un palindrome.")


# import string
# import time
#
#
# def creer_table_de_translation():
#     # Créer une table de traduction pour ignorer les caractères accentués et autres
#     accents = str.maketrans("àäéèëïôùüç", "aaeeeiouuc", string.punctuation + string.whitespace)
#     return accents
#
#
# def est_palindrome(phrase):
#     # Convertir l'entrée en minuscules et appliquer la table de traduction
#     phrase = phrase.lower().translate(creer_table_de_translation())
#     return phrase == phrase[::-1]  # Utiliser une comparaison pour vérifier le palindrome
#
#
# total_duration = 0
#
# for _ in range(1000):
#     start = time.time()
#
#     mot = input("Entrez un mot ou une phrase (ou 'x' pour quitter) : ")
#
#     # Vérifiez si l'utilisateur veut quitter
#     if mot.lower() == 'x':
#         print("Au revoir !")
#         break  # Sortez de la boucle while pour quitter le programme
#
#     if est_palindrome(mot):
#         print("Le mot ou la phrase est un palindrome.")
#     else:
#         print("Le mot ou la phrase n'est pas un palindrome.")
#
#     end = time.time()
#     duration = end - start
#     total_duration += duration
#
# # Calculer le temps d'exécution moyen
# average_duration = total_duration / 1000
# print(f"Le programme s'est exécuté en moyenne en {average_duration} secondes par test.")
