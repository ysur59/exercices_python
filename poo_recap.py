#!/usr/bin/env python

from random import random
from time import sleep

"""
Biologie des dragons, des humains et des moutons.
"""

ROMAN = 'IVXLCM'


def hasard(max):
    """
    Donne un nombre au hasard entre 0 et un maximum.

    :param int max: un maximum
    :rtype: int
    """
    return int(random()*max)


def rand_extract(liste):
    """
    Extrait aléatoirement un élément d'une liste, et retourne le tout séparément.

    :param list liste: une liste à découper
    :returns: l'élement extrait, le reste de la liste
    :rtype: type, [type]
    """
    indice = hasard(len(liste))
    element = liste.pop(indice)
    return element, liste


class Animal(object):

    """
    Classe générique pour tous les animaux.
    """
    ESPECE = 'animal'

    def __init__(self, nom):
        self.nom = nom
        self.age = 0
        self.esperence_de_vie = 100

    @classmethod
    def generate_name():
        raise NotImplementedError

    def veillir(self):
        """
        Veillit d'un an l'animal.

        :returns: Retourne vrai si l'animal est toujours en vie.
        :rtype: bool
        """
        self.age = self.age + 1
        if self.age > self.esperence_de_vie:
            return False

        return True

    def peut_manger(self, consommable):
        """
        Consomme un animal.

        :param Animal consommable: l'animal consommé
        :returns: Retourne vrai si l'animal est réellement consommé.
        :rtype: bool
        """
        if not isinstance(consommable, Animal):
            print("Je ne mange pas de cette chaire là")
            return False

        return True

    def __repr__(self):
        return '<{} {} / {} ans>'.format(
            self.ESPECE.capitalize(),
            self.nom,
            self.age
        )


class Dragon(Animal):

    """
    Je crois que je viens de voir un dragon.
    """

    ESPECE = 'dragon'
    NOMS_DE_DRAGON = ['Smaug', 'Alduin', 'Odahviing']

    def __init__(self, nom):
        Animal.__init__(self, nom)
        self.esperence_de_vie = 256

    @classmethod
    def generate_name(cls):
        return '{}_{}'.format(
            cls.NOMS_DE_DRAGON[hasard(len(cls.NOMS_DE_DRAGON))],
            ROMAN[hasard(len(ROMAN))]
        )


class Humain(Animal):

    """
    Je cherche un Homme.
    """

    ESPECE = 'humain'
    NOMS_HUMAIN = ['Elrindir', 'Babette', 'Général Tullius', 'Colette Marence', 'Sorine Jurard', 'Nazir']

    def __init__(self, nom):
        Animal.__init__(self, nom)
        self.esperence_de_vie = 60

    @classmethod
    def generate_name(cls):
        return '{}_{}'.format(
            cls.NOMS_HUMAIN[hasard(len(cls.NOMS_HUMAIN))],
            hasard(10)
        )

    def peut_manger(self, consommable):
        """
        :rtype: bool
        """
        if not isinstance(consommable, Mouton):
            print("Je ne mange que du mouton")
            return False

        return True


class Mouton(Animal):

    """
    On compte plus facilement ses moutons que ses amis.
    """
    ESPECE = 'mouton'
    NOMS_MOUTON = ['Vincent van', 'Baaarnabas', 'Mephistopheles', 'Nibbler', 'Skooter']

    def __init__(self, nom):
        Animal.__init__(self, nom)
        self.esperence_de_vie = 10

    @classmethod
    def generate_name(cls):
        return '{}_{}-{}'.format(
            cls.NOMS_MOUTON[hasard(len(cls.NOMS_MOUTON))],
            hasard(10), hasard(100)
        )

    def peut_manger(self, consommable):
        if isinstance(consommable, Animal):
            print("Je ne mange pas de chaire")
            return False

        return True


# Initialisation
dragons = []
for i in range(3):
    dragons.append(Dragon(nom=Dragon.generate_name()))

humains = []
for i in range(2):
    humains.append(Humain(nom=Humain.generate_name()))

moutons = []
for i in range(5):
    moutons.append(Mouton(nom=Mouton.generate_name()))

# moutons[0].peut_manger(dragons[0])

encore_une_annee = True

while encore_une_annee:

    print("\n=== Une nouvelle année arrive ===")
    print(
        "Il y a {} dragons, {} humains, et {} moutons."
        .format(len(dragons), len(humains), len(moutons))
    )

    # Vieillissement
    for animal in dragons + humains + moutons:
        if not animal.veillir():
            del animal

    # Naissances
    nb_bebe = int(len(humains) / 2)
    nb_agneau = int(len(moutons) / 2) * 2

    for i in range(nb_bebe):
        humains.append(Humain(nom=Humain.generate_name()))

    for i in range(nb_agneau):
        moutons.append(Mouton(nom=Mouton.generate_name()))

    # Les dragons se repaissent
    for dragon in dragons:
        # S'il y a plus de moutons, ceux-ci ont de plus grandes 
        # chances d'être mangé
        if hasard(len(moutons)+len(humains)) <= len(moutons):
            animal, moutons = rand_extract(moutons)
        else:
            animal, humains = rand_extract(humains)
        if dragon.peut_manger(animal):
            print('{} mange {}'.format(dragon, animal))

    # Les humains se repaissent
    if len(humains) > 0:
        nb_méchoui = int(len(moutons) / 4) + 1

        for i in range(nb_méchoui):
            if len(moutons) == 0:
                break
            animal, moutons = rand_extract(moutons)
            if humains[0].peut_manger(animal):
                print('{} est mangé en méchoui'.format(animal))

    # Fin
    if len(dragons) == 0:
        print("Il n'y a plus de dragons !")
        encore_une_annee = False
    elif len(humains) == 0:
        print("Il n'y a plus d'humains !")
        encore_une_annee = False
    elif len(moutons) == 0:
        print("Il n'y a plus de moutons !")
        encore_une_annee = False

    sleep(5)

print('\n >>>>> Résultat final <<<<<')
print(dragons)
print(humains)
print(moutons)
