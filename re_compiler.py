#!bin/python2.7

"""

CS212 Udacity Design of computer Programs 
Module 3 - Problem 3 
Regular Expression API implementation - Compiler Form

"""

from re_api import search, test_search

def match(pattern, text):
    "Match pattern against start of text; return longest match found or None."
    remainders = pattern(text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:len(text)-len(shortest)]

def lit(s): return lambda text: set(text[len(s):]) if text.startswith(s) else null
def seq(x, y): return lambda text: set().union(*map(y, x(text)))
def alt(x, y): return lambda text: x(text) | y(text)
def oneof(chars): return lambda text: set(text[1:]) if (text and text[0] in chars) else null
dot = lambda text: set(text[1:]) if text else null
eol = lambda text: set(['']) if text else null 

def star(x): return lambda text: (set([text]) | 
                                  set(t2 for t1 in x(text) if t1 != text
                                      for t2 in star(x)(t1)))

if __name__ == '__main__':
    print test_search()
