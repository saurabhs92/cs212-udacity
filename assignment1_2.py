#!bin/python2.7

# Poker Homework 1, Problem 2: Jokers

## Deck adds two cards: red and black jokers
## '?B': black joker; can be used as any black card (C or S)
## '?B': red   joker; can be used as any red   card (D or H)

import itertools
from poker import hand_rank
from assignment1_1 import best_hand

allranks   = '23456789TJQKA'
redcards   = [r+s for r in allranks for s in 'DH']
blackcards = [r+s for r in allranks for s in 'SC']

def best_wild_hand(hand):
    "Try all values for jokers for all 5 card selections."
    # Apply replacements to every card in a hand and retun a list; 
    # Apply best hand on all possible combinations found using product ()
    hands = set(best_hand(h) for h in (itertools.product(*map(replacements, hand))))
    return max(hands, key=hand_rank)

def replacements(card):
    "Return a list of all possible replacements for a card (More than 1 for jokers)"
    if   card == '?B' : return blackcards
    elif card == '?R' : return redcards
    else : return [card]

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())) 
            == ['7C', '8C', '9C', 'JC', 'TC']) 
    assert (sorted(best_wild_hand("TD TC 5H 7C 7D ?R ?B".split())) 
            == ['7C', 'TC', 'TD', 'TH', 'TS']) 
    assert (sorted(best_wild_hand("TD TC TH 7C 7D 7S 7H".split())) 
           == ['7C', '7D', '7H', '7S', 'TD']) 
    return 'test_best_wild_hand passes'

print test_best_wild_hand()
    
