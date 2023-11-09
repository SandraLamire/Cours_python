PRIX_CAFE = 0.6
PIECES = [2, 1, 0.5, 0.2, 0.1, 0.05]
montant = 0


def rendu_monnaie(monnaie, piece_fournie):
    nb_pieces = int((monnaie - monnaie % piece_fournie) / piece_fournie)
    monnaie -= nb_pieces * piece_fournie
    print(str(nb_pieces) + " pièce(s) de " + str(piece_fournie))
    return monnaie


while montant < PRIX_CAFE:
    montant_piece = float(input("Prix du café : 0.60€\n"
                                "Entrez la valeur de la pièce :\n"
                                "(Pièces acceptées : 2€, 1€, 0.50€, 0.20€, 0.10€ et 0.05€)\n"))

    if montant_piece in PIECES:
        montant += montant_piece
        if montant >= PRIX_CAFE:
            monnaie_a_rendre = montant - PRIX_CAFE
            print("Voici votre café et votre monnaie : (" + format(monnaie_a_rendre, ".2f") + "€): \n")
            for piece in PIECES:
                monnaie_a_rendre = rendu_monnaie(monnaie_a_rendre, piece)
        else:
            print("Crédit insuffisant (" + format(montant, ".2f") + "€)")

    else:
        print("Piece non reconnue\n")

