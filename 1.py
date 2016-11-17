#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import os

data = [1]
if len(data) == 2:
    print data[1]
else:
    print data[0]

'''
    参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

比如定义一个函数，包含上述若干种参数：
'''


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)

#for循环中的k应该是引用传递
data = [{"1": 1}, {"2": 2}, {"3": 3}]
for k in data:
    k['v'] = 'v'
print data

#k传递的是值
data = [1, 2, 3, 5, 5]
for k in data:
    print k
    k = 1
print data

#继承自object


class Sun(object):

    def __init__(self, *args):
        pass

    def __getAttr__(self):
        pass
print Sun().__class__

print int(time.time())
#self指向类对象


