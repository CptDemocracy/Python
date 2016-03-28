"""
[ref.] https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def IsPrime(n):
    if n & 1:
        lim = int(n ** .5)
        for m in xrange(3, lim + 1, 2):
            if n % m == 0:
                return False
        return True
    else:
        return n == 2
      
def FindLargestPrimeFactor(n):
    if n < 2:
        raise ValueError("n cannot be smaller than the smallest prime 2")
    m = int(n ** .5) | 1
    while m >= 3:
        if IsPrime(m) and n % m == 0:
            return m
        m -= 2
    if n % 2 == 0:
        return 2
    return -1

n = 600851475143L
ans = FindLargestPrimeFactor(n) # 6857
print "The largest prime factor for %d is %d." % (n, ans)
