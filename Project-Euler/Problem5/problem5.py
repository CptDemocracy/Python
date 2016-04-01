"""
[ref.href] https://projecteuler.net/problem=5

Smallest multiple.

2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""

EPS = 1e-6

def IsDivisibleByAll(n, divs):
    for div in divs:
        if n % div != 0:
            return False
    return True

def GCD(n, m, eps = EPS):
    if ((abs(n) >= 0 and abs(n) <= eps) or
        (abs(m) >= 0 and abs(m) <= eps)):
        return 0
    while n % m > eps:
        temp = m
        m = n % m
        n = temp
    return m

def LCD(n, m, eps = EPS):
    gcd = GCD(n, m, eps)
    if abs(gcd) >= 0 and abs(gcd) <= eps:
        return 1
    return n * m / gcd

lowestdiv = 1
highestdiv = 20
divs = range(lowestdiv, highestdiv + 1)
lcd = reduce(LCD, divs)
print "The smallest positive number that is evenly divisible by " +\
    ", ".join([str(div) for div in divs]) + " is " + str(lcd) + "."
