#!bin/python2.7

# Homework Assigment 1 
# Write the best_hand function which takes in a 7 card hand and returns the best 5 card hand. 

def best_hand(hand):
    "From a 7 card hand, return the best 5 card hand."

def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split())) == ['6C', '7C', '8C', '9C', 'TC']) 
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split())) 
           == ['8C', '8C', 'TC', 'TD', 'TH']) 
    assert (sorted(best_hand("TD TC TH 7C 7D 7S 7H".split())) 
           == ['7C', '7D', '7H', '7S', 'TD']) 
    return 'test_best_hand passes'

print test_best_hand()
