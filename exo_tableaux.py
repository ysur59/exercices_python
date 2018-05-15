#!/usr/bin/env python

"""
Écrire dans un tableau un liste de prénom et dans un autre, une liste d‘animaux.
Gérer des surnoms aléatoire avec.
"""

from random import random

prenoms = ['Dédé', 'Firmin', 'Léon', 'Agathe', 'Didier', 'Conan']
animaux = ['la galinette cendrée', 'le lémurien', 'le frelon', 'la blatte', 'le bourdon', 'le barbare']

for i in range(4):
    print(
        prenoms[int(random()*len(prenoms))],
        animaux[int(random()*len(animaux))]
    )
