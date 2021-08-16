'''
Write function that checks if a given string (case insensitive) is a palindrome.
'''

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]