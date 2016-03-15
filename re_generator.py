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

def genseq(x, y, Ns, startx=0):
    "Set of matches to xy whose total len in in Ns."
    if not Ns:
        return null
    xmatches = x(set(range(startx, max(Ns)+1)))
    Ns_x = set(len(m) for m in xmatches)
    Ns_y = set(n-m for n in Ns for m in Ns_x if n-m >= 0)
    ymatches = y(Ns_y)
    return set(m1 + m2 
               for m1 in xmatches for m2 in ymatches
               if len(m1+m2) in Ns)

def test_gen():
    def N(hi): return set(range(hi+1))
    a,b,c = map(lit, 'abc')
    assert star(oneof('ab'))(N(2)) == set(['', 'a', 'aa', 'ab',
                                           'ba', 'bb', 'b'])
    return 'test_gen_passes'

