#!/usr/bin/env python

"""
Programme dénombrant le nombre de voyelles dans une phrase
"""

vowels = 'aeiou'

ip_str = input("Taper une phrase: ")
ip_str = ip_str.casefold()

count = {}.fromkeys(vowels, 0)

for char in ip_str:
    if char in count:
        count[char] += 1

print("Voici les résultats: ", count)
