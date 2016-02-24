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

# Method 1

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

# Method 2 (faster, better, compiles each formula only once so that eval - the most time consuming function - is called only once per formula.)

def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string. Output formula is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula."""
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass

def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also returns letters found, as a str, 
    in same order as parms of function. For example, 'YOU == ME**2' returns
    (lambda Y, O, U, M, E: (U+10*O+100*Y) == (E+10*M)**2), 'YMEOU' """
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print f
    return eval(f), letters

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
        print '%6.4f sec :  %s' % timecall(faster_solve, example)
    print '%6.4f tot.' % (time.clock() - t0)

cProfile.run('test()')
