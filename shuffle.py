#!bin/python2.7

# Different implementations of the function random.shuffle
# shuffle() is correct
# Functions shuffle1-3 are incorrect implementations


import random

def shuffle(deck):
    "Knuth's Algorithm P."
    N = len(deck)
    for i in range(N-1):
        swap(deck, i, random.randrange(i, N))

def shuffle1(deck):
    "Incorrect algorithm!"
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)

def swap(deck, i, j):
    "Swap elements i, j of a collection."
    print 'swap', i, j
    deck[i], deck[j] = deck[j], deck[i]


        
