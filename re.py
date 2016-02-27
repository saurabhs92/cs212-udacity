#!bin/python2.7

"""

CS212 Udacity Design of computer Programs 
Module 3 - Problem 1 
Regular Expressions

"""

def search(pattern, text):
    "Return True if pattern appears anywhere in text."

def match(pattern, text):
    "Return True if pattern appears at the start of the text."
    
def test():
    assert search('baa*!', 'Sheep said baaa!')
    assert search('baa*!', 'Sheep said baaaa humbug') == False
    assert match('baa*!', 'Sheep said baaaa!') == False
    assert match('baa*!', 'baaaaaaaa! said the sheep')
