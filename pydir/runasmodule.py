#!/usr/bin/python
# -*- coding: utf-8 -*-
print('''we can use __name__=="__main__" to check run as an mode''')

def PrintAuthor(name):
    print(name)

if __name__ == "__main__":
    PrintAuthor('Rainy')

