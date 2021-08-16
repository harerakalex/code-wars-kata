'''
Task
John is a typist. He has a habit of typing: he never use the Shift key to switch case, just using only Caps Lock.

Given a string s. Your task is to count how many times the keyboard has been tapped by John.

You can assume that, at the beginning the Caps Lock light is not lit.

Input/Output
[input] string s

A non-empty string. It contains only English letters(uppercase or lowercase).

1 ≤ s.length ≤ 10000

[output] an integer

The number of times John tapped the keyboard.

Example
For s = "a", the output should be 1.

John hit button a.

For s = "aa", the output should be 2.

John hit button a, a.

For s = "A", the output should be 2.

John hit button Caps Lock, A.

For s = "Aa", the output should be 4.

John hit button Caps Lock, A, Caps Lock, a.
'''

def typist(s):
    counter = 0
    for i in range(len(s)):
        if s[i].isupper() and i < (len(s) - 1) and s[i+1].isupper():
            counter += 1
        elif s[i].isupper() and i < (len(s) - 1) and s[i+1].islower():
            counter += 3
        elif s[i].isupper():
            counter += 2
        else:
            counter += 1
    
    return counter