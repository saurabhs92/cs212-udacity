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
    assert match(abcstars, 'aaabbccccccdef') == 'aaabbcccccc'
    assert match(abcstars, 'junk') == ''
    assert all(match(seq(abcstars, eol), s) == s for s in 'abc aaabbccc aaaabcccccc'.split())
    assert all(match(seq(abcstars, eol), s) == None for s in 'cab aaabbcccd aaaa-b-cccccc'.split())
    r = seq(lit('ab'), seq(dotstar, seq(lit('aca'), seq(dotstar, seq(a, eol)))))
    assert all(search(r, s) is not None for s in 'abracadabra abaca about-acacia-flora'.split())
    assert all(match(seq(c, seq(dot, b)), s) is not None for s in 'cab cob carob cb carbuncle'.split())
    assert not any(match(seq(c, seq(dot, b)), s) for s in 'crab cb across scab'.split())
    return 'test_search passes.'


