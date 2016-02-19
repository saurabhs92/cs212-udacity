#!bin/python2.7

# Poker Homework 1, Problem 2: Jokers

## Deck adds two cards: red and black jokers
## '?B': black joker; can be used as any black card (C or S)
## '?B': red   joker; can be used as any red   card (D or H)

def best_wild_hand(hand):
    "Try all values for jokers for all 5 card selections."
    

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())) 
            == ['6C', '7C', '8C', '9C', 'TC']) 
    assert (sorted(best_wild_hand("TD TC 5H 7C 7D ?R JB".split())) 
            == ['7C', 'TC', 'TD', 'TH', 'TS']) 
    assert (sorted(best_wild_hand("TD TC TH 7C 7D 7S 7H".split())) 
           == ['7C', '7D', '7H', '7S', 'TD']) 
    return 'test_best_wild_hand passes'

print test_best_wild_hand()
    
