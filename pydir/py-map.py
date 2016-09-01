print('''
This program introduces a function list(proc, existinglist)
''')
#!/usr/bin/python
# -*- coding: utf-8 -*-
def normalize(name):
    return name.capitalize();

words = ['abc', 'Kitty', 'really']
newwords = list(map(normalize, words))
print('Old words:')
print(words)
print('New words:')
print(newwords)
