'''

This is my republished first kata(with issues fixed!), hope you guys will enjoy it!

For input, you will be given a string in the form "(mx+n)(px+q)" where the character x can be any single lowercase alphabet from a-z, while m, n, p and q are integers(can be negative).

Task
Return a string in the format ax^2+bx+c where a, b and c are integers, eg. 5x^2-6x+8
If a or b is 1, the '1' in front of the variable should be omitted. eg. x^2+x-20
If a or b is -1, only the minus sign - should be shown, eg. -x^2-x+6
Examples:
quadratic_builder("(x+2)(x+3)")  #return "x^2+5x+6"
quadratic_builder("(x-2)(x+7)")  #return "x^2+5x-14"
quadratic_builder("(3y+2)(y+5)")  #return "3y^2+17y+10"
quadratic_builder("(-h-7)(4h+3)")  #return "-4h^2-31h-21"
'''

import re
def quadratic_builder(expression):
    #Good Luck!!
        
    # get separate expression enclosed in ()
    a,b = re.findall('\(.*?\)', expression)
    
    # Remain where contain a number in first part
    
    unknown_variable = re.findall('[a-zA-z]', a)
    find_negative = re.sub('-[a-zA-z]', '-1{}'.format(unknown_variable[0]), a)
    part1 = re.findall('-?\d+', find_negative)
    
    if len(part1) == 2:
        m = int(part1[0])
        n = int(part1[1])
    else:
        m = 1
        n = int(part1[0])

    unknown_variable = re.findall('[a-zA-z]', b)
    find_negative = re.sub('-[a-zA-z]', '-1{}'.format(unknown_variable[0]), b)
    part1 = re.findall('-?\d+', find_negative)
    
    if len(part1) == 2:
        p = int(part1[0])
        q = int(part1[1])
    else:
        p = 1
        q = int(part1[0])

    # formatting the result in form of ix^2 + hx + j
    i = m * p
    if i == 1:
        ix = '{}'.format(unknown_variable[0])
    elif i == -1:
        ix = '-{}'.format(unknown_variable[0])
    else:
        ix = '{}{}'.format(i, unknown_variable[0])

    h = (m*q) + (n * p)
    if h > 1:
        hx = '+{}{}'.format(h, unknown_variable[0])
    elif h == 1:
        hx = '+{}'.format(unknown_variable[0])
    elif h == -1:
        hx = '-{}'.format(unknown_variable[0])
    elif h == 0:
        hx = ''
    else:
        hx = '{}{}'.format(h, unknown_variable[0])
    
    j = n * q
    if j > 0:
        j = '+{}'.format(j)
    elif j == 0:
        j = ''

    return '{}^2{}{}'.format(ix, hx, j)