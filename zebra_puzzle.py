#!bin/python2.7

"""
CS212 Udacity Design of computer Programs 
Module 2

 Zebra Puzzle
1 There are five houses.
2 The Englishman lives in the red house.
3 The Spaniard owns the dog.
4 Coffee is drunk in the green house.
5 The Ukrainian drinks tea.
6 The green house is immediately to the right of the ivory house.
7 The Old Gold smoker owns snails.
8 Kools are smoked in the yellow house.
9 Milk is drunk in the middle house.
10 The Norwegian lives in the first house.
11 The man who smokes Chesterfields lives in the house next to the man with the fox.
12 Kools are smoked in a house next to the house where the horse is kept.
13 The Lucky Strike smoker drinks orange juice.
14 The Japanese smokes Parliaments.
15 The Norwegian lives next to the blue house.
 Who drinks water? Who owns the zebra?

Each house is painted a different color, and their inhabitants are of different nationalities, own different pets, drink different beverages and smoke different brands of American cigarettes. 
"""

import itertools
import time

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))

def imright(h1, h2):
    "House h1 is immediately right of h2 of h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1
    
def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA) indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)       # 6
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegnian) in orderings 
                if (Englishman is red)         # 2
                if nextto(Norwegnian, blue)    #15
                if (Norwegnian is first)       #10
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if (Spaniard is dog)           # 3
                for (coffee, tea, milk, oj, WATER) in orderings
                if (Ukranian is tea)           # 5
                if (milk is middle)            # 9
                if (coffee is green)           # 4
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if (OldGold is snails)         # 7
                if (Kools is yellow)           # 8
                if nextto(Chesterfields, fox)  #11
                if nextto(Kools, horse)        #12
                if (LuckyStrike is oj)         #13
                if (Japanese is Parliaments)   #14
                )

# WATER, ZEBRA = zebra_puzzle()
# print WATER, ZEBRA

def timecall(fn, *args):
    "Calculate the time to execute a function."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int; 
    or upto n seconds if n is a float; return min, avg and max times."""
    if isinstance(n, int):
        times = [timecall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while(sum(times) < n):
            times.append(timecall(fn, *args)[0])
    return min(times), average(times), max(times)

def average(numbers):
    "Return arithmetic mean of a sequence of numbers."
    return sum(numbers) / float(len(numbers))
"""
def instrument_fn(fn, *args):
    c.starts, c.items = 0, 0
    result = fn(*args)
    print '%s got %s with %5d iters over %7d items.' % (
        fn.__name__, result, c.starts, c.items)
# zebra_puzzle got (1, 5) with 25 iters over 2775 items.    

def c(sequence):
    "Generate items in sequence, keeping counts. c.starts, c.items are no. of seq started & items generated."
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item
"""

print timecall(zebra_puzzle)
print timedcalls(100, zebra_puzzle)
print timedcalls(10.0, zebra_puzzle)
# instrument_fn(zebra_puzzle)
