#!bin/python2.7

import random

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
    deck[i], deck[j] = deck[j], deck[i]

