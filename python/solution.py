'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''

def solution(string,markers):
    n_list = []
    for sentence in string.split("\n"):
        s = ""
        for word in sentence:
            if word in markers:
                break
            else:
                s = s + word
        n_list.append(s.strip())
    return "\n".join(n_list)