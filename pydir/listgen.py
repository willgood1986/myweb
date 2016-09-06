# -*- coding: utf-8 -*-
print("List generate: [x for x in 'abc']")
print([ x + "&" + y for x in 'ABC' for y in '123'])
print("list-generator operates on list")
datas = {'a':1, 'b':2, 'c':3}
print("Get data[key, val] from dict use dict.items")
print([y+2 for x, y in datas.items()])
