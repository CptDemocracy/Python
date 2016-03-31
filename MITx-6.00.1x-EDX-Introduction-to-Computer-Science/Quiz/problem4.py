"""
Quiz Problem 4.

Write a simple procedure, myLog(x, b), that computes the logarithm of 
a number x relative to a base b. For example, if x = 16 and b = 2, 
then the result is 4 - because 24=16. If x = 15 and b = 3, then the 
result is 2 - because 32 is the largest power of 3 less than 15.

In other words, myLog should return the largest power of b such that 
b to that power is still less than or equal to x.

x and b are both positive integers; b is an integer greater than or 
equal to 2. Your function should return an integer answer.

Do not use Python's log functions; instead, please use an iterative 
or recursive solution to this problem that uses simple arithmatic 
operators and conditional testing.
"""

def myLog(x, b):
    '''
    x, b: pos ints
    b >= 2
    returns: int; log_b(x)
    implemented via: iterative or recursive algorithm
    '''
    if type(x) != int or type(b) != int or b < 2 or x < 0:
        raise ValueError
    if x < b:
        return 0
    i = 1
    prod = b
    while prod * b <= x:
        prod *= b
        i += 1
    return i
