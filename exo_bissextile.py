#!/usr/bin/env python

"""
Programme testant si une année saisie par l'utilisateur est bissextile ou non
"""

annee = input("Saisissez une année : ")
annee = int(annee)
bissextile = False

if annee % 4 == 0:
    bissextile = True

    if annee % 100 == 0 and annee % 400 != 0:
        bissextile = False

else:
    bissextile = False


if bissextile:
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")
