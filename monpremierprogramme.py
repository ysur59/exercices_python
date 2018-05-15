#!/usr/bin/env python

"""
Ce programme calcule le périmètre d'un cercle dont le rayon a été
demandé au clavier à l'utilisateur.
"""

import math


def perimetre_cercle(un_rayon):
    """
    Calcule le périmètre d'un cercle à partir de son rayon.

    :param un_rayon: le rayon du cercle (positif)
    :return le périmètre d'un cercle de rayon un_rayon
    :rtype: float
    """
    diametre = 2 * un_rayon
    return math.pi * diametre


def main():
    """Le programme principal."""
    # demander le rayon à l'utilisateur
    saisie = input("Quel est le rayon du cercle : ")
    # saisie est une chaîne de caractères
    le_rayon = float(saisie)
    # convertie en un nombre réel

    perimetre = perimetre_cercle(le_rayon)

    print("Le périmètre d'un cercle de rayon", le_rayon, "est", perimetre)

if __name__ == "__main__":
    print("Bonjour. Je vais calculer pour vous le périmètre d'un cercle.")
    main()
