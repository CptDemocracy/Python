"""
[ref.href] https://projecteuler.net/problem=2

Even Fibonacci numbers.

Each new term in the Fibonacci sequence is generated by adding
the previous two terms. By starting with 1 and 2, the first 10
terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
"""

def FibonacciGenerator(n):
    yield 0
    a = 0
    b = 1
    fib = a + b
    while fib < n:
        fib = a + b
        yield fib
        temp = a
        a = fib
        b = temp

lim = 4000000
fgen = FibonacciGenerator(lim)
fnums = []
for fib in fgen:
    if fib % 2 == 0:
        fnums.append(fib)
sm = sum(fnums)

print "The sum of even fibonacci numbers that do not exceed %d is equal to %d." % (lim, sm)
