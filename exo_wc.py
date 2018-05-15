#!/usr/bin/env python

"""
Compter le nombre de lignes et de mots dans un fichier.
"""

def count_lines(filename):
    f = open(filename)
    n = len(f.readlines())
    f.close()
    return n


def count_words(filename):
    f = open(filename)
    n = 0

    for line in f.readlines():
        n = n + len(line.split(' '))

    f.close()
    return n

filename = 'monpremierprogramme.py'
print("Il y a {} lignes dans le fichier '{}', et {} mots."
    .format(
        count_lines(filename),
        filename,
        count_words(filename)
    )
)
