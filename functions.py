def return_values(nom, prenom=""):
    return nom, prenom


nom, prenom = return_values("Doe", "John")
print("Bonjour", prenom, nom)


def afficher_liste(*args):
    for objet in args:
        print("- ", objet)


afficher_liste("chocolat", "carotte", 17)

