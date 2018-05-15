#!/usr/bin/env python

"""
Accède à l'api RickAndMorty pour récupérer des informations et générer un
fichier csv avec.

Pour tous les lieux de type planète, lister les informations des personnages
vivants qui y habitent ainsi que le nom, le code et la date de diffusion du
premier épisode où ils apparaissent.
Le format du fichier csv sera le suivant:
Nom,Espèce,Type,Genre,Lieu,CodeEpisode,NomEpisode,DateDeDiffusion
Format de date: YYYY-MM-DD
Le nom du ficher de sortie est définit en paramètre.
"""

import csv
import datetime
import requests
from argparse import ArgumentParser

URL_API = 'http://localhost:8080'
INCLUDED_STATUS = ['Alive']
EXCLUDED_SPECIES = ['Human']


class EnrichedCharacter(object):

    """
    R&M character with first episode data.
    """

    def __init__(self, character, episode):
        self.character = character
        self.episode = episode

    @property
    def episode_date(self):
        """
        :rtype: datetime
        """
        return datetime.datetime.strptime(self.episode['air_date'], '%B %d, %Y')

    def csv_row(self):
        """
        Format character data as a single csv row
        :rtype: list
        """
        return [
            self.character['name'],
            self.character['species'],
            self.character['type'],
            self.character['gender'],
            self.character['location']['name'],
            self.episode['episode'],
            self.episode['name'],
            self.episode_date.strftime('%Y-%m-%d')
        ]


def get_api(url):
    """
    Generic API getter.
    :param str url: url to call
    :returns: a dict or a list of results
    """
    return requests.get(url).json()


def get_all_locations(filter_=''):
    """
    Get all locations.
    :param str filter_: location filter
    :rtype: list
    """
    return get_api(URL_API + '/api/location/?' + filter_)


def get_character(id_=''):
    """
    Get one or multiple characters.
    :param str id_: id of a character
    :rtype: dict or list
    """
    return get_api(URL_API + '/api/character/' + id_)


def main(output_file):
    characters = []
    planets = get_all_locations(filter_='?type=Planet').get('results')

    residents = []
    for planet in planets:
        ids = [x.split('/')[-1] for x in planet['residents']]
        residents = residents + ids
    residents = list(set(residents))
    #print(residents)

    for resident in residents:
        character = get_character(id_=resident)
        if character is None or len(character['episode']) == 0:
            continue
        if character['status'] not in INCLUDED_STATUS or character.get('species') in EXCLUDED_SPECIES:
            continue

        episode = get_api(url=character['episode'][0])  # first episode
        if episode is None:
            continue

        enriched_character = EnrichedCharacter(
            character=character,
            episode=episode
        )
        characters.append(enriched_character)
    #print(characters)

    with open(output_file, 'w', newline='') as csvfile:
        spamwriter = csv.writer(
            csvfile,
            delimiter=',',
            quoting=csv.QUOTE_MINIMAL
        )
        spamwriter.writerow(['Nom', 'Espèce', 'Type', 'Genre', 'Lieu', 'CodeEpisode', 'NomEpisode', 'DateDeDiffusion'])
        spamwriter.writerows([i.csv_row() for i in characters])
    csvfile.close()

if __name__ == "__main__":
    parser = ArgumentParser(description='Rick&Morty API scrapper')
    parser.add_argument("--csvfile", help='Path for output csv file')
    args = parser.parse_args()

    main(args.csvfile)
