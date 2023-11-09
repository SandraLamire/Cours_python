##########################################################################
# Nombres premiers
def est_nombre_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
    return True


nombres_premiers = [n for n in range(1001) if est_nombre_premier(n)]

print("Nombres premiers entre 0 et 1000 :\n")
print(nombres_premiers)

##########################################################################
# Nombres premiers avec saisie des limites
min1 = int(input("Saisir le nombre minimum :\n"))
max1 = int(input("Saisir le nombre maximum :\n"))
nombres_premiers_avec_range = [n for n in range(min1, max1) if est_nombre_premier(n)]

print(f"Nombres premiers entre {min1} et {max1} :\n")
print(nombres_premiers_avec_range)


##########################################################################
# Trouver un nombre premier
def trouver_nombres_premiers(n):
    list_nbs_premiers = []
    nb = 2
    while len(list_nbs_premiers) < n:
        if est_nombre_premier(nb):
            list_nbs_premiers.append(nb)
        nb += 1
    return list_nbs_premiers


nb_premier_1000_eme = trouver_nombres_premiers(1000)

# vérifier que le 1000ème nombre premiers est 7919
if nb_premier_1000_eme[-1] == 7919:
    print("Le 1000ème nombre premier est bien 7919.")
else:
    print("Le 1000ème nombre premier n'est pas 7919!")
