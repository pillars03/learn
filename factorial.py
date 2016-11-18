#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 5


def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n - 1))
print factorial(a)
