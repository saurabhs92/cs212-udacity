#!bin/python2.7

# CS212 Udacity Design of computer Programs 
# Module 2 - Homework assignment 2 
# 
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Please do not use regular expressions to solve this quiz!
# 0123k56789
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    text = text.lower()
    spaces = text.count(' ') 
    spaces += 1
    print spaces
    size = len(text)
    print size 
    i, j = 0, 0
    start, stop = 0, 0
    for k in range(size):
        n = 1
        print 'k = ' + str(k)
        while (k-n>=0 and k+n<=size):
            print '  n = ' + str(n)
            string = text[k-n:k+n+1]
            print '  ' + string
            if (string == string[::-1]): 
                start, stop = k-n, k+n
                print '  ' + str(start) + ' ' + str(stop)
            n += 1
        if ((stop - start) > (j - i)): i, j = start, stop
    return i, j + 1
        

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
print longest_subpalindrome_slice('racecar')
print longest_subpalindrome_slice('Race carr')
