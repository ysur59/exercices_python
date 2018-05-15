#!/usr/bin/env python

"""
À partir d'une liste de serveur (list de dict), générer une url en fonction du port.
Si c'est sur le port ssh, le lien est de type ssh, sinon, c'est un lien http
"""

data = [
    {
        'host': '10.0.0.2',
        'port': 22
    },
    {
        'host': 'tamla.motown.org',
        'port': 8347
    },
    {
        'host': '172.16.8.4',
        'port': 2164
    }
]
