#!/usr/bin/env python

"""
prend un entier en paramètre, en calcul la racine, 
et écrit le résultat dans un fichier, si un nom de 
fichier est passé en paramètre, sur la sortie standard sinon.
"""

import datetime
import math
from argparse import ArgumentParser

parser = ArgumentParser(description='ma racine')
parser.add_argument('-i', '--integer', required=True, type=int, nargs=1)
parser.add_argument('-o', '--output')

args = parser.parse_args()

resultat = math.sqrt(args.integer[0])
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
message = '{} - {}\n'.format(now, resultat)

if args.output:
	with open(args.output, 'a+') as file:
		file.write(message)
	file.close()
else:
	print(message)
