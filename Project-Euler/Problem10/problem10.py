"""
[ref.href] https://projecteuler.net/problem=10

Summation of primes.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

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

primegen = PrimeGenerator()
upperBound = 2000000
primesum = 0
for prime in primegen:
    if prime >= upperBound:
        break
    primesum += prime

print "The sum of all primes below " + str(upperBound) + " is " + str(primesum) + "."
