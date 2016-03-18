#!bin/python2.7

"""

CS212 Udacity Design of computer Programs 
Module 3 - Problem 4 
Cache Memoization

"""

#from re_api import decorator
from functools import update_wrapper

def decorator(d):
    """Make function d a decorator; d wraps a function fn.
    Updates help of both the fn d and the fn that d is applied to."""
    def _d(fn):
        return update_wrapper(d(fn), d)
    return update_wrapper(_d, d)

@decorator
def memo(f):
    """Decorator that catches the return value of each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            return f(*args)
    return _f

@decorator
def countcalls(f):
    "Decorator that makes the function countcalls to it, in countcalls[f]."
    def _f(*args):
        callcounts[_f] += 1
        return f(*args)
    callcounts[_f] = 0
    return _f

callcounts = {}

@countcalls
@memo
def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)

a = fib(5)
print a 
