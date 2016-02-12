#!bin/python2.7

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
sf = "TC JC QC KC AC".split()

def poker(hands):
    "Return the best hand: poker([hand,.. ]) => hand"
    return max(hands, key=hand_rank)

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
    return ranks

def straight(ranks):
    "Return true if the ranks form a straight"
    minrank = min(ranks)
    maxrank = max(ranks)
    mid = (minrank + maxrank) / 2
    num = len(ranks)
    avg = (sum(ranks)) / num
    diff = maxrank - minrank + 1
    return ((avg == mid) and (diff == num))

def flush(hand):
    "Return true if the suit is same for all cards"
    firstsuit = hand[0][1:]  # Compare all suits with first card's suit 
    for card in hand:
        suit = card[1:]
        #print suit
        if suit != firstsuit:
            return False
    return True
        
def two_pair(ranks):
    "Return true if there are two 2 of a kinds in the ranks"

def kind(n, ranks):
    "Returns the rank of the card that appears n times in a hand"


def test():
    "Test cases for testing out all possible combinations"
    sf = "6C 7C 8C 9C TC".split() # Straight flush
    fk = "9C 9H 9S 9T 7D".split() # Four of a kind
    fh = "TD TH TC 7C 7D".split() # Full house
    # Test the card_ranks function
    assert card_ranks (sf) == [10,  9,  8, 7, 6]
    assert card_ranks (fk) == [ 9,  9,  9, 9, 7]
    assert card_ranks (fh) == [10, 10, 10, 7, 7]
    """
    # Test the poker function
    assert poker ([sf, fk, fh]) == sf
    assert poker ([fk, fh])     == fk
    assert poker ([fh, fh])     == fh
    assert poker ([fh])         == fh
    assert poker ([fh]*100)     == fh
    """
    # Test straight and flush functions
    assert straight ([9,8,7,6,5]) == True
    assert straight ([9,8,6,4,3]) == False
    assert flush (sf)             == True
    assert flush (fk)             == False
    """
    # Test the hand_rank function (yet to be fixed) 
    assert hand_rank (sf) == (8, 10)
    assert hand_rank (fk) == (7, 9, 7)
    assert hand_rank (fh) == (6, 10, 7)
    """
    return "Tests pass"

print test()
print sf
print card_ranks(sf)

