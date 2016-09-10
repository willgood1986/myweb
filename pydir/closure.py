# -*- coding: utf-8 -*-
# There are two points:
# 1 We should return the function name
# 2 The returned function must be called with ()
def closure():
    results = []
    for i in range(1, 4):
        def f():
            # i is a reference 
            return i ** 2
        # f is a reference
        results.append(f)
    return results

def independentclosure():
    def f(i):
        def g():
            return i ** 2
        return g

    results = []
    for i in range(1, 4):
        # invoke here
        results.append(f(i))
    return results


if __name__ == '__main__':
    a, b, c = closure()
    # call
    print(a())
    print(b())
    print(c())

    a1, b1, c1 = independentclosure()
    print(a1())
    print(b1())
    print(c1())

