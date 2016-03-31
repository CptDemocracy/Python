"""
Problem 5.

Write a generator, genPrimes, that returns the sequence of prime numbers 
on successive calls to its next() method: 2, 3, 5, 7, 11, ...
"""

def isPrime(n):
    lim = n
    for i in range(2, lim):
        if n % i == 0:
            return False
    return True
    
def genPrimes():
    n = 2
    while True:
        if isPrime(n):
            yield n
        n += 1
        
# [revision notice 31/03/2016 (dd/mm/yyyy)]
# the isPrime function is rather inefficient, below's
# my revised version of the function:
#
# def isPrime(n):
#   if n % 2 == 0:
#     return n == 2
#   lim = int(n ** 0.5)
#   for i in xrange(3, lim + 1, 2):
#     if n % i == 0:
#       return False
#   return True
