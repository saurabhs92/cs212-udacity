#!bin/python2.7

"""

CS212 Udacity Design of computer Programs 
Module 3 - Problem 3 
Regular Expressions - Generators

"""

def lit(s):       
    set_s = set([s])
    return lambda Ns: set_s if len(Ns) in Ns else null
def alt(x, y):    return lambda Ns: x(Ns) | y(Ns)
def star(x):      return lambda Ns: opt(plus(x))(Ns)
def oneof(chars): 
    set_chars = set(chars)
    return lambda Ns: set_chars if 1 in Ns else null
def opt(x):       return alt(epsilon, x)
def seq(x, y):    return lambda Ns: genseq(x, y, Ns)
def plus(x):      return lambda Ns: genseq(x, star(x), Ns, startx=1)
dot = oneof('?')  # Add as many characters as you want
epsilon = lit('') # The pattern which matches empty string.
