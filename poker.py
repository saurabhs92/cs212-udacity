#!bin/python2.7

import random

"""

CS212 Udacity Design of computer Programs 
Define a poker program 

Basics:-
hand = 5 cards  eg. 5D, 6H, 8D, 2C, 9H
A card has a rank and a suit
poker(hands) -> hand # returns the best hand


Hand rank concept - hands have ranks of the following types  
n-kind 22  33  888
straight 56789
flush 	 5 diamonds or 5 hearts etc

"""

sf = "6C 7C 8C 9C TC".split() # Straight flush
fk = "9C 9H 9S 9T 7D".split() # Four of a kind
    
def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    result, maxval = [], None
    key = key or (lambda x: x)  # Use the key passed or use the identity fn
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result

def hand_rank(hand):
    "Return a value indicating the rank of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
    return 

def card_ranks(hand):
    "Return a list of ranks in a hand, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    # Handle the straight A-5 case
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def straight(ranks):
    "Return true if the ordered ranks form a 5-card straight."
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    "Return true if the suit is same for all cards."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1
        
def two_pair(ranks):
    """If there are two pairs, return the two ranks as a tuple:
    (highest, lowest); otherwise return None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

def kind(n, ranks):
    """Returns the first rank of the card that appears n times in a hand.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def test():
    "Test cases for testing out all possible combinations"
    sf = "6C 7C 8C 9C TC".split() # Straight flush
    fk = "9C 9H 9S 9T 7D".split() # Four of a kind
    fh = "TD TH TC 7C 7D".split() # Full house
    tp = "5D 5C 8H 8C 6S".split() # Two pair
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    # Test the card_ranks function
    assert card_ranks (sf) == [10,  9,  8, 7, 6]
    assert card_ranks (fk) == [ 9,  9,  9, 9, 7]
    assert card_ranks (fh) == [10, 10, 10, 7, 7]
    # Test the poker function
    assert poker ([sf, fk, fh]) == [sf]
    assert poker ([fk, fh])     == [fk]
    assert poker ([fh, fh])     == [fh, fh]
    assert poker ([fh])         == [fh]
    assert poker ([fh]*100)     == [fh]*100
    # Test straight and flush functions
    assert straight ([9,8,7,6,5]) == True
    assert straight ([9,8,6,4,3]) == False
    assert flush (sf)             == True
    assert flush (fk)             == False
    # Test the hand_rank function 
    assert hand_rank (sf) == (8, 10)
    assert hand_rank (fk) == (7, 9, 7)
    assert hand_rank (fh) == (6, 10, 7)
    # Test the kind and two_pair functions
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (8, 5)
    return "Tests pass"

print test()
print 'Straight flush: ' + str(sf)
print 'Four of a kind: ' + str(fk)
print 'Output of card_ranks (sf)  : ' + str(card_ranks(sf))
print 'Output of poker ([sf, fk]) : ' + str(poker([sf, fk]))
print 'Output of hand_rank (sf)   : ' + str(hand_rank(sf))
