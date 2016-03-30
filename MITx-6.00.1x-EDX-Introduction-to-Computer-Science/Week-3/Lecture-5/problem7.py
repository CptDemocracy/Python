"""
Problem 7.

For this problem, write a recursive function, lenRecur, which computes
the length of an input argument (a string), by counting up the number
of characters in the string.
"""

def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr == "":
        return 0
    return 1 + lenRecur(aStr[1:])
