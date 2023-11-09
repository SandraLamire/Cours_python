import string


def nettoyer_phrase(phrase):
    # Créer une table de traduction pour ignorer les caractères accentués et autres
    accents = str.maketrans("", "", string.punctuation + string.whitespace)

    # Supprimer les caractères non lettrés et convertir en minuscules
    phrase = phrase.lower().translate(accents)

    return phrase


def comptabiliser_lettres(phrase):
    # Utiliser un dictionnaire pour comptabiliser le nb de chaque lettre
    compteur = {}
    for lettre in phrase:
        compteur[lettre] = compteur.get(lettre, 0) + 1
    return compteur


def sont_anagrammes(phrase1, phrase2):
    phrase1 = nettoyer_phrase(phrase1)
    phrase2 = nettoyer_phrase(phrase2)

    compteur1 = comptabiliser_lettres(phrase1)
    compteur2 = comptabiliser_lettres(phrase2)

    # Comparer les dictionnaires
    return compteur1 == compteur2


# Tester avec exemples
# Testez avec des exemples
phrase3 = "Chien"
phrase4 = "Niche"
if sont_anagrammes(phrase3, phrase4):
    print(f"{phrase3} et {phrase4} sont des anagrammes.")
else:
    print(f"{phrase3} et {phrase4} ne sont pas des anagrammes.")

# Exemple avec des caractères accentués
phrase5 = "Élysées"
phrase6 = "Yeélssa"
if sont_anagrammes(phrase5, phrase6):
    print(f"{phrase5} et {phrase6} sont des anagrammes.")
else:
    print(f"{phrase5} et {phrase6} ne sont pas des anagrammes.")