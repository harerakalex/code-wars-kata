'''
Your function takes two arguments:

current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).
'''

def twice_as_old(dad_years_old, son_years_old):
    years_ago = 2 * son_years_old - dad_years_old
    return years_ago if years_ago >= 0 else years_ago * -1 