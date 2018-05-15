#!/usr/bin/env python

"""
Lire le fichier /etc/passwd, extraire le nom des users, leur id et leur home, puis
générer un fichier json avec toutes les données (list de dict).
"""

import json
import re

PASSWD_LINE = re.compile("^(.+):x:(\d+):\d*:.*:(.*):.*$", re.MULTILINE)
# ex: root:x:0:0:root:/root:/bin/bash


def main():
    with open('/etc/passwd', 'r') as file:
        content = file.read()
    file.close()

    users = []

    for line in PASSWD_LINE.finditer(content):
        user, id_, home = line.groups()
        try:
            id_ = int(id_)
        except ValueError:
            id_ = -1
        users.append({
            'user': user,
            'id': id_,
            'home': home
        })

    with open('output.json', 'w+') as file:
        file.write(json.dumps(users))
    file.close()

if __name__ == "__main__":
    main()
