'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''

import string

def high(x):    
    group_word = [(a, word_length(a)) for a in x.split()]
    highest = 0
    word = ''
    for a,b in group_word:
        if b > highest: 
            highest = b
            word = a

    return word
    
def word_length(word: str):
    return sum([char_position(c) for c in word])
    
def char_position(char: str):
    return string.ascii_lowercase.index(char.lower()) + 1