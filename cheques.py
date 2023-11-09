nb_cheques = 0
montant_total = 0
nb_petit_cheques = 0
montant_total_petits_cheques = 0
nb_gros_cheques = 0
montant_total_gros_cheques = 0
numero_plus_petit_cheque = 0
montant_plus_petit_cheque = 0
numero_plus_gros_cheque = 0
montant_plus_gros_cheque = 0

numero_cheque = int(input("Saisir le numéro du chèque :\n"))

while numero_cheque != 0:
    # pass = permet de ne pas remplir le block mais de pouvoir compiler et run quand même
    montant_cheque = float(input("Quel est le montant du chèque?\n"))
    nb_cheques += 1
    montant_total += montant_cheque

    if montant_cheque > montant_plus_gros_cheque:
        montant_plus_gros_cheque = montant_cheque
        numero_plus_gros_cheque = numero_cheque
    else:
        montant_plus_petit_cheque = montant_cheque
        numero_plus_petit_cheque = numero_cheque

    if montant_cheque < 200:
        montant_total_petits_cheques += montant_cheque
        nb_petit_cheques += 1
    else:
        montant_total_gros_cheques += montant_cheque
        nb_gros_cheques += 1

    numero_cheque = int(input("Saisir le numéro du chèque :\n"))

if nb_cheques == 0:
    print("Aucun chèque de saisi !")
else:
    print("somme des chèques : " + str(montant_total))
    print("nombre de chèques : " + str(nb_cheques))
    moyenne = round(montant_total / nb_cheques, 2)
    print("moyenne : " + str(moyenne))
    print("somme des chèques < 200€ : " + str(montant_total_petits_cheques))
    print("nombre de chèques < 200€ : " + str(nb_petit_cheques))
    print("somme des chèques >= 200€ : " + str(montant_total_gros_cheques))
    print("nombre de chèques >= 200€ : " + str(nb_gros_cheques))
    print("Le plus petit cheque porte le numéro " + str(numero_plus_petit_cheque) + " et son montant est de : " + str(montant_plus_petit_cheque) + "€")
    print("Le plus grand cheque porte le numéro " + str(numero_plus_gros_cheque) + " et son montant est de : " + str(montant_plus_gros_cheque) + "€")
