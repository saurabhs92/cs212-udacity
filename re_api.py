#!bin/python2.7

"""

CS212 Udacity Design of computer Programs 
Module 3 - Problem 2 
Regular Expressions - APIs

"""

def test_search():
    a, b, c  = lit(a), lit(b), lit(c)
    abcstars = seq(star(a), seq(star(b), star(c)))
    dotstar  = star(dot)
    assert search(lit('def'), 'abcdef') == 'def'
    assert search(seq(lit('def'), eol), 'abcdef') == 'def'
    assert search(a, 'not the start') == 'a'
    assert match(a, 'not the start') == None
    assert match(abcstars, 'aaabbccccccdef') == aaabbcccccc
    assert match(abcstars, 'junk') == ''
    
