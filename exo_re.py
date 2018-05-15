#!/usr/bin/env python

"""
Écrire un programme qui va vérifier qu‘une chaîne saisie par 
l‘utilisateur est au bon format, et afficher les groupes.

Format: Les mots commencent tous par une majuscules, les 
chiffres et le mot suivant forment un groupe.
"""

import re

BON_FORMAT = re.compile('([A-Z0-9])\w*')
GROUPES = re.compile('([0-9]+ \w+)')

phrase = "Nous, Si Vous Réfléchissez Bien, On A 4 Bras."


def est_bien_formatté(phrase):
	"""
	Dit si la phrase est bien formatté.

	:param str phrase: la phrase a analyser
	:rtype: bool
	"""
	for mot in phrase.split(' '):
		if BON_FORMAT.match(mot) is None:
			return False

	return True

debut_phrase = "La phrase n'est pas au bon format"
if est_bien_formatté(phrase):
	debut_phrase = 'La phrase est au bon format'

groupes = re.findall(GROUPES, phrase)
if len(groupes) > 0:
	message = '{}. Groupes: {}'.format(debut_phrase, groupes)
else:
	message = phrase

print(message)
