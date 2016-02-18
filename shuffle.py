#!bin/python2.7

# Different implementations of the function random.shuffle
# shuffle() is correct
# Functions shuffle1-3 are incorrect implementations


import random
from collections import defaultdict

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
    #print 'swap', i, j
    deck[i], deck[j] = deck[j], deck[i]

def test_shuffler(shuffler, deck='abcd', n=10000):
    "Test a shuffler algorithm n times with a deck of strings and print result (ok/bad) and the %age."
    counts = defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1
    expcounts = n * 1. / factorial(len(deck))
    print 'deck : ' + deck
    ok = all((0.9 <= counts[item]/expcounts <= 1.1) for item in counts)
    name = shuffler.__name__
    print '%s(%s) : %s' % (name, deck, ('OK' if ok else 'BAD'))
    
    for item, count in sorted(counts.items()):
        print '%s:%4.1f' % (item, count * 100./n),
    print

def factorial(n): return 1 if (n <= 1) else n * factorial(n-1)

def test_shufflers(shufflers=[shuffle, shuffle1], decks=['abcd', 'abc']):
    for deck in decks:
        print
        for f in shufflers:
            test_shuffler(f, deck)

test_shufflers()
