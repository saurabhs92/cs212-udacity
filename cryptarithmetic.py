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

import string, re

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string. Output formula is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f

def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    

def valid(formula):
    "Formula is valid iff it has no leading zero, and evaluates to True."
    try:
        # ensure no number starts with 0
        return not re.search(r'\b0[0-9]', formula) and eval(f) is True 
    except ArithmeticError:    # Division-by-zero, overflows, etc.
        return False

