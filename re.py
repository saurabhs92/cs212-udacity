#!bin/python2.7

"""

CS212 Udacity Design of computer Programs 
Module 3 - Problem 1 
Regular Expressions

"""

def search(pattern, text):
    "Return True if pattern appears anywhere in text."
    if pattern.startswith('^'): 
        return match(pattern[1:], text)
    else:
        return match('.*' + pattern, text)

def match(pattern, text):
    "Return True if pattern appears at the start of the text."
    if (pattern == ''):
        return True
    elif pattern == '$':
        return (text == '')
    elif len(pattern) > 1 and pattern[1] in '*?':
        p, op, pat = pattern[0], pattern[1], pattern[2:]
        if (op == '*'):
            return match_star(p, pattern, text)
        elif (op == '?'):
            if (match1(p, text) and match(pat, text[1:])):
                return True
            else:
                return match(pat, text)
    else:
        return (match1(pattern[0], text) and 
                match(pattern[1:], text[1:]))
    
        
def test():
    assert search('baa*!', 'Sheep said baaa!')
    assert search('baa*!', 'Sheep said baaaa humbug') == False
    assert match('baa*!', 'Sheep said baaaa!') == False
    assert match('baa*!', 'baaaaaaaa! said the sheep')
    assert search('def', 'abcdefg') 
    assert search('def$', 'abcdef') 
    assert search('def$', 'abcdefg') == False
    assert search('^start', 'not the start') == False
    assert match('start', 'not the start') == False
    assert match('a*b*c*', 'just anything') 
    assert match('x?', 'text') 
    assert match('text?', 'text')
    assert match('text?', 'text')
    def words(text): return words.split()
    assert all(match('aa*bb*cc*$', s) for s in words('abc aabbcc aaabcccc'))
    assert not any(match('aa*bb*cc*$', s) for s in words('abc aabbcc aaabcccc'))
    assert all(match('^ab.*aca.*a$', s) for s in words('abracadabra abacaa about-acacia-fa'))
    assert all(match('t.p', s) for s in words('tip top tap atypical tepid stop'))
    assert not any(match('t.p', s) for s in words('TYPE teepee tp'))
    return 'test passes'


