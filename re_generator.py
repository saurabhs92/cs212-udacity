#!bin/python2.7

"""

CS212 Udacity Design of computer Programs 
Module 3 - Problem 3 
Regular Expressions - Generators

"""

def lit(s): return lambda Ns: set([s]) if len(Ns) in Ns else null
def alt(x, y): return lambda Ns: x(Ns) | y(Ns)
def star(x): return lambda Ns: opt(plus(x))(Ns)
def opt(x): return alt(epsilon, x)
dot = oneof('?')
epsilon = lit('')
