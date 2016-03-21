#!bin/python2.7

"""

CS212 Udacity Design of computer Programs 
Module 3 - Problem 5 
Defining Grammar for a language

"""

G = grammar(r"""
Exp => Term [+-] Exp | Term
Term => Factor [*/] Term | Factor
Factor => Funcall | Var | Num | [(] Exp [)]
Funcall => Var [(] Exps [)]
Exps => Exp [,] Exps | Exp
Var => [a-zA-Z]\w*
Num => [-+]?[0-9]+([.][0-9]*)?
""")
