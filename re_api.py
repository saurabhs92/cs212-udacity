#!bin/python2.7

"""

CS212 Udacity Design of computer Programs 
Module 3 - Problem 2 
Regular Expressions APIs - Interpretter Implementation

"""

from functools import update_wrapper

def n_ary(f):
    """Given binary function f(x,y), return an n_ary function such that
    f(x,y,z) = f(x, f(y,z)), etc. Also allow f(x)=x"""
    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))
    update_wrapper(n_ary_f, f)
    return n_ary_f

def lit(x):       return ('lit', x)

@n_ary
def seq(x, y):    return ('seq', x, y)

@n_ary
def alt(x, y):    return ('alt', x, y)
def star(x):      return ('star', x)
def plus(x):      return (seq(x, star(x)))
def oneof(chars): return ('oneof', chars)
dot = ('dot',)
eol = ('eol',) 

def matchset(pattern, text):
    "Match pattern at start of text; return a set of remainders of text."
    op, x, y = components(pattern)
    if 'lit' == op:
        return set([text[len(x):]]) if text.startswith(x) else null
    elif 'seq' == op:
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        matchset(x, text) | matchset(y, text)
    elif 'dot' == op:
        return set([text[1:]]) if text else null
    elif 'oneof' == op:
        return set([text[1:]]) if any(text.startswith(c) for c in x) else null
    elif 'eol' == op:
        return set(['']) if text == '' else null
    elif 'star' == op:
        return set([text]) | set(t2 for t1 in matchset(x, text) 
                                 for t2 in matchset(pattern, t1) if t1 != text)
    else:
        raise ValueError('unknown pattern: %s' % pattern)

null = frozenset()

def search(pattern, text):
    "March pattern anywhere in text; return longest earliest match or None."
    for i in range(len(text)):
        m = match(pattern, text[i:])
        if m is not None:
            return m

def match(pattern, text):
    "Match pattern against start of text; return longest match found or None."
    remainders = matchset(pattern, text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:len(text)-len(shortest)]

def components(pattern):
    "Return the op, x, y arguments; x and y are None if missing."
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y

def test_search():
    a, b, c  = lit('a'), lit('b'), lit('c')
    abcstars = seq(star(a), seq(star(b), star(c)))
    dotstar  = star(dot)
    assert search(lit('def'), 'abcdef') == 'def'
    assert search(seq(lit('def'), eol), 'abcdef') == 'def'
    assert search(a, 'not the start') == 'a'
    assert match(a, 'not the start') == None
    assert match(abcstars, 'aaabbccccccdef') == 'aaabbcccccc'
    assert match(abcstars, 'junk') == ''
    assert all(match(seq(abcstars, eol), s) == s for s in 'abc aaabbccc aaaabcccccc'.split())
    assert all(match(seq(abcstars, eol), s) == None for s in 'cab aaabbcccd aaaa-b-cccccc'.split())
    r = seq(lit('ab'), seq(dotstar, seq(lit('aca'), seq(dotstar, seq(a, eol)))))
    assert all(search(r, s) is not None 
               for s in 'abracadabra abacaa about-acacia-flora'.split())
    assert all(match(seq(c, seq(dot, b)), s) is not None 
               for s in 'cab cob cabrob ccb cabrbuncle'.split())
    assert not any(match(seq(c, seq(dot, b)), s) 
                   for s in 'crab cb across scab'.split())
    return 'test_search passes.'

if __name__ == '__main__':
    print test_search()
