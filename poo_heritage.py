#!/usr/bin/env python3

"""
Faire une classe Véhicule et adapter les classes Voiture 
et Avion précédentes pour utiliser l‘héritage.
"""

class Vehicule(object):

    """
    Classe générique des véhicules.
    """

    réservoire = 0

    def démarrer(self):
        raise NotImplementedError

    def remplir_reservoir(self, quantité):
        self.réservoire = quantité

    def changer_un_pneu(self, nouveau_pneu, emplacement):
        pass


class Avion(Vehicule):
    
    """
    Représentation d'un avion.
    """

    modèle = "Airbus"

    def rentrer_le_train_d_aterrissage(self):
        pass

    def démarrer(self):
        pass


class Voiture(Vehicule):

    """
    Représentation d'une voiture.
    """

    marque = "Jaguar"

    def ouvrir_le_coffre(self):
        pass

    def démarrer(self):
        pass


avion = Avion()
avion.remplir_reservoir(27.32)
print(avion.réservoire)
