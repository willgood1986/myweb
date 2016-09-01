# -*- coding: utf-8 -*-
def normalize(name):
    return name.capitalize();

words = ['abc', 'Kitty', 'really']
words = list(map(normalize, words))
print words
