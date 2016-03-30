"""
Problem 5.

Write a Python function, clip(lo, x, hi) that returns lo if x is 
less than lo; hi if x is greater than hi; and x otherwise. For 
this problem, you can assume that lo < hi.
"""

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return max(lo, min(x, hi))
