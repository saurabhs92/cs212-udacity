#!bin/python2.7

"""

CS212 Udacity Design of computer Programs 
Module 3 - Problem 5 
Defining Grammar for a language

"""

G = grammar(r"""
Exp => Term [+-] Exp | Term
""")
