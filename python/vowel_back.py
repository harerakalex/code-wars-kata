'''
You need to play around with the provided string (s).

Move consonants forward 9 places through the alphabet. If they pass 'z', start again at 'a'.

Move vowels back 5 places through the alphabet. If they pass 'a', start again at 'z'. For our Polish friends this kata does not count 'y' as a vowel.

Exceptions:

If the character is 'c' or 'o', move it back 1 place. For 'd' move it back 3, and for 'e', move it back 4.

If a moved letter becomes 'c', 'o', 'd' or 'e', revert it back to it's original value.

Provided string will always be lower case, won't be empty and will have no special characters.
'''

from string import ascii_lowercase

def vowel_back(st: str):
    new_str = ''
    for i in range(len(st)):
        if st[i] == 'c' or st[i] == 'o':
            new_str = new_str + get_movable_char(st[i], -1)
        elif st[i] == 'd':
            new_str = new_str + get_movable_char(st[i], -3)
        elif st[i] == 'e':
            new_str = new_str + get_movable_char(st[i], -4)
        elif st[i] not in 'aeiou':
            new_str = new_str + get_movable_char(st[i], 9)
        elif st[i] in 'aeiou':
            new_str = new_str + get_movable_char(st[i], -5)

    return new_str

def get_char_position(char: str) -> int:
    return ascii_lowercase.index(char)

def get_movable_char(char, move):
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    if get_char_position(char) in range(17, 26) and char not in 'code':
        movable_char = alpha[(get_char_position(char) - len(alpha)) + move]
    elif char in 'aeiou' and get_char_position(char) in range(0, 5) and char not in 'code':
        movable_char = alpha[(get_char_position(char) + len(alpha)) + move]
    else:
        movable_char = alpha[get_char_position(char) + move]

    if movable_char in 'code':
        movable_char = char
    print(char, '|',  get_char_position(char) , '|' , movable_char)

    return movable_char