#!bin/python2.7

"""

CS212 Udacity Design of computer Programs 
Module 3 - Problem 5 
Defining Grammar for a language

"""


def split(text, sep=None, maxsplit=-1):
    "Like str.split applied to text, but strips whitespace from each peace."
    return [t.strip() for t in text.strip().split(sep, maxsplit) if t]


def grammar(description, whitespace=r'\s*'):
    """Convert a description to a grammar."""
    G = {' ': whitespace}
    description = description.replace('\t', ' ') # no tabs
    for line in split(description, '\n'):
        lhs, rhs = split(line, '=>', 1)
        alternatives = split(rhs, ' | ')
        G[lhs] = tuple(map(split, alternatives))
    return G


G = grammar(r"""
Exp => Term [+-] Exp | Term
Term => Factor [*/] Term | Factor
Factor => Funcall | Var | Num | [(] Exp [)]
Funcall => Var [(] Exps [)]
Exps => Exp [,] Exps | Exp
Var => [a-zA-Z]\w*
Num => [-+]?[0-9]+([.][0-9]*)?
""")

def print_dict(dict):
    for (k, v) in dict.items():
        print k 
        print v

print_dict(G)
