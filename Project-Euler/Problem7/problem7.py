"""
[ref.href] https://projecteuler.net/problem=7

10001st prime.

By listing the first six prime numbers:

2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def IsPrime(n):
    if n & 1:
        lim = int(n ** 0.5)
        m = 3
        while m <= lim:
            if n % m == 0:
                return False
            m += 2
        return True
    else:
        return n == 2

def PrimeGenerator(nthPrime = None):

    if nthPrime == None:
        cond = lambda c: True
    else:
        cond = lambda c: c < nthPrime

    n = 1
    if cond(n) == False:
        return
    
    yield 2
    
    candidate = 3
    while cond(n):
        if IsPrime(candidate):
            n += 1
            yield candidate
        candidate += 2

nthprime = 10001
primegen = PrimeGenerator(nthprime)
prime = 2
n = 1
for prime in primegen:
    pass
print "The %d prime number is %d." % (nthprime, prime)
