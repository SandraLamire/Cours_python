POIDS_BOEUF = 500
COEF_BOEUF_BLEU = 10 / POIDS_BOEUF
COEF_BOEUF_A_POINT = 17 / POIDS_BOEUF
COEF_BOEUF_BIEN_CUIT = 25 / POIDS_BOEUF

POIDS_PORC = 400.0
COEF_PORC_BLEU = 15 / POIDS_PORC
COEF_PORC_A_POINT = 25 / POIDS_PORC
COEF_PORC_BIEN_CUIT = 40 / POIDS_PORC

POIDS_CANARD = 450.0
COEF_CANARD_BLEU = 20 / POIDS_CANARD
COEF_CANARD_A_POINT = 25 / POIDS_CANARD
COEF_CANARD_BIEN_CUIT = 30 / POIDS_CANARD


viande = input("Entrer un type de viande :\nBoeuf, Porc ou Canard\n").lower()
poids_viande = float(input("Entrer un poids :\n"))
cuisson = input("Entrer une cuisson :\n 1 : Bleu, 2 : A point ou 3 : Bien cuit : \n")

if viande == "boeuf":
    if cuisson == "1":
        tempsCuisson = poids_viande * COEF_BOEUF_BLEU
        print("Le temps de cuisson est de : " + str(tempsCuisson) + " minutes")

    elif cuisson == "2":
        tempsCuisson = poids_viande * COEF_BOEUF_A_POINT
        print("Le temps de cuisson est de : " + str(tempsCuisson) + " minutes")

    elif cuisson == "3":
        tempsCuisson = poids_viande * COEF_BOEUF_BIEN_CUIT
        print("Le temps de cuisson est de : " + str(tempsCuisson) + " minutes")

    else:
        print("Cette cuisson n'est pas connue")

elif viande == "porc":
    if cuisson == "1":
        tempsCuisson = poids_viande * COEF_PORC_BLEU
        print("Le temps de cuisson est de : " + str(tempsCuisson) + " minutes")

    elif cuisson == "2":
        tempsCuisson = poids_viande * COEF_PORC_A_POINT
        print("Le temps de cuisson est de : " + str(tempsCuisson) + " minutes")

    elif cuisson == "3":
        tempsCuisson = poids_viande * COEF_PORC_BIEN_CUIT
        print("Le temps de cuisson est de : " + str(tempsCuisson) + " minutes")

    else:
        print("Cette cuisson n'est pas connue")

elif viande == "canard":
    if cuisson == "1":
        tempsCuisson = poids_viande * COEF_CANARD_BLEU
        print("Le temps de cuisson est de : " + str(tempsCuisson) + " minutes")

    elif cuisson == "2":
        tempsCuisson = poids_viande * COEF_CANARD_A_POINT
        print("Le temps de cuisson est de : " + str(tempsCuisson) + " minutes")

    elif cuisson == "3":
        tempsCuisson = poids_viande * COEF_CANARD_BIEN_CUIT
        print("Le temps de cuisson est de : " + str(tempsCuisson) + " minutes")

    else:
        print("Cette cuisson n'est pas connue")

else:
    print("Cette viande n'est pas connue")
