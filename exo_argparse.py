#!/usr/bin/env python

"""
prend un entier en paramètre, en calcul la racine, 
et écrit le résultat dans un fichier, si un nom de 
fichier est passé en paramètre, sur la sortie standard sinon.
"""

import math
from argparse import ArgumentParser

parser = ArgumentParser(description='ma racine')
parser.add_argument('-i', '--integer', required=True, type=int, nargs=1)
parser.add_argument('-o', '--output')

args = parser.parse_args()

resultat = math.sqrt(args.integer[0])
if args.output:
	with open(args.output, 'w+') as file:
		file.write(str(resultat))
	file.close()
else:
	print(resultat)
