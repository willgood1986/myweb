# -*- coding: utf-8 -*-
# move box...
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return

   #when 2, a->b, a->c, b->c
    move(n - 1, a, c, b)
    print(a, '-->', c)
    move(n - 1, b, a, c)


if __name__ == '__main__':
    move(2, 'A', 'B', 'C') 
