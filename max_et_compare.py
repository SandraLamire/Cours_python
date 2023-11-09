from random import randrange

# Fonction max
def nb_max(a, b):
    max_number = max(a, b)
    return max_number


# Fonction compare
def compare_values(a, b):
    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return -1


# Fonction max et compare
def max_et_compare(a, b):
    max_val = nb_max(a, b)
    compare_val = compare_values(a, b)
    print(f"Valeur max: {max_val}")
    print(f"Comparaison des valeurs: {compare_val}")

nb_aleatoire = lambda limite=99999: randrange(-1 * limite, limite + 1) # nb_aleatoire()

nb1 = nb_aleatoire()
nb2 = nb_aleatoire()
print(f"Premier nombre : {nb1}, second nombre : {nb2}")
max_et_compare(nb1, nb2)

