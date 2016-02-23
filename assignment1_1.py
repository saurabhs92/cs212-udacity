#!bin/python2.7

"""
CS212 Udacity Design of computer Programs 
Module 1 - Homwork assignment 1 

Write the best_hand function which takes in a 7 card hand and returns the best 5 card hand. 
"""

from poker import hand_rank
import itertools

def best_hand(hand):
    "From a 7 card hand, return the best 5 card hand."
    return max(itertools.combinations(hand, 5), key=hand_rank)

def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split())) 
            == ['6C', '7C', '8C', '9C', 'TC']) 
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split())) 
           == ['8C', '8S', 'TC', 'TD', 'TH']) 
    assert (sorted(best_hand("TD TC TH 7C 7D 7S 7H".split())) 
           == ['7C', '7D', '7H', '7S', 'TD']) 
    return 'test_best_hand passes'

if __name__ == '__main__':
    print test_best_hand()
