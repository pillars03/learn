#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a test module'

__author__='Pillars Sun'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':
    test()


class Student(object):

    def __init__(self, name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print "%s:%s" %(self.name,self.score)
bart=Student('Bart Simpson',59)
bart.print_score()

print dir('abc')
