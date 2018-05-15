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


def generate_url(host, port):
    """
    Generate an url based on a hostname and a port.

    :param str host: the hostname
    :param str port: a specific port
    :rtype: str
    """
    url = ''
    if port == 22:
        url = 'ssh://{host}:{}'.format(port, host=host)
    else:
        url = 'http://{host}:{}'.format(port, host=host)

    return url


def main():
    urls = []
    for serveur in data:
        url = generate_url(
            hotsname=serveur['host'],
            port=serveur['port']
        )
        urls.append(url)

    print(urls)

if __name__ == "__main__":
    main()
