#!bin/python2.7

"""
CS212 Udacity Design of computer Programs 
Module 2 - Problem 2 
Cryptarithmetic Problems

The following equation is of cryptharithmetic type:

 ODD
+ODD
----
EVEN

Solution of cryptarithmetic problems assigns a digit to each letter of an arithmetic equation like above. 
The equation should be correct and different letters should correspond to different digits:

 655
+655
----
1310

We will try substituting letters with all combinations of digits and use eval to evaluate which combination satisfies the equation. 
"""

from __future__ import division
from zebra_puzzle import timecall
import string, re, itertools, time, cProfile

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string. Output formula is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f

def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)
        
def valid(f):
    "Formula is valid iff it has no leading zero, and evaluates to True."
    try:
        # ensure no number starts with 0
        return not re.search(r'\b0[0-9]', f) and eval(f) is True 
    except ArithmeticError:    # Division-by-zero, overflows, etc.
        return False

def compile_word(word):
    """Complle a word of uppercase letters as digits.
    E.g., compile_word('YOU') => '(1*U + 10*O + 100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if(word.isupper()):
        terms = ['%s*%s' % (10**i, d) for i, d in (enumerate(word[::-1]))]
        return '(' + '+'.join(terms) + ')'
    else:
        return word

examples = """ TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == CY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()

def test():
    t0 = time.clock()
    for example in examples:
        print; print 13*' ', example
        print '%6.4f sec :  %s' % timecall(solve, example)
    print '%6.4f tot.' % (time.clock() - t0)

cProfile.run('test()')
