#!/usr/bin/env python
# -*- coding: utf-8 -*-


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print str2int("123")

inIter = ['adam', 'LISA', 'barT']


def regNames(iter):
    return map((lambda inStr: inStr.capitalize()), iter)
print regNames(inIter)

inIter = [1, 2, 3, 4, 5]
prod = lambda iter: reduce((lambda x, y: x * y), iter)
print prod(inIter)


# filter
def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])


def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j
            return g
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print f1()
print f2()
print f3()
