"""
Problem 9.

Write a Python function, odd, that takes in one number and returns 
True when the number is odd and False otherwise.

You should use the % (mod) operator, not if.

This function takes in one number and returns a boolean.
"""

def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    return bool(int(x) % 2)
    
# [revision notice 31/03/2016 (dd/mm/yyyy)]
# It's fun looking back at your old code, especially now
# that you know of better solutions. Another solution
# would be to write the function like this:
#
# def odd(x):
#   return bool(x & 1)
