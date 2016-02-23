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

def valid(formula):
    "Formula is valid iff it has no leading zero, and evaluates to True."
    try:
        return not re.search(r'\b0[0-9]', formula) and eval(f) is True
    except ArithmeticError:
        return False

