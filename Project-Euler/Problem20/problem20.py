"""
[ref.href] https://projecteuler.net/problem=20

Factorial digit sum.

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

def GetFactorial(n):
    if n < 2:
        return 1
    return n * GetFactorial(n - 1)

num = 100
fac = GetFactorial(num)
sm = 0
while fac > 0:
    sm += fac % 10
    fac //= 10
print "The sum of the digits in the number %d! is %d." % (num, sm)
