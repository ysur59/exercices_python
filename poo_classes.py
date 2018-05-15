#!/usr/bin/env python3

"""
Contruire les classes représentant une voiture et un avion.
Donner au moins deux attributs pour chaque classe, dont un commun aux deux classes
Donner au moins quatre méthodes pour chaque classe, dont deux communes aux deux classes
"""

class Avion(object):
    
    """
    Représentation d'un avion.
    """

    réservoire = 0
    modèle = "Airbus"

    def rentrer_le_train_d_aterrissage(self):
        pass

    def démarrer(self):
        pass

    def remplir_reservoir(self, quantité):
        pass

    def changer_un_pneu(self, nouveau_pneu, emplacement):
        pass


class Voiture(object):

    """
    Représentation d'une voiture.
    """

    réservoire = 0
    marque = "Jaguar"

    def ouvrir_le_coffre(self):
        pass

    def démarrer(self):
        pass

    def remplir_reservoir(self, quantité):
        pass

    def changer_un_pneu(self, nouveau_pneu, emplacement):
        pass


voiture = Voiture()
print(voiture.marque)
voiture.démarrer()
