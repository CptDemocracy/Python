"""
[ref.] https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def ReverseNumber(num):
    if num < 0:
        num = -num
    result = 0
    while num > 0:
        result *= 10
        result += num % 10
        num //= 10
    return result

def IsNumberPalindromic(n):
    return n == ReverseNumber(n)

def FindLargestPalindromicNumber(muldigits):
    minmul = int(10 ** (muldigits - 1))
    maxmul = int(10 ** muldigits - 1)

    mulrange = xrange(minmul, maxmul + 1)

    # since we are looking for the largest palindrome
    # we will start at the top
    rmulrange = reversed(mulrange)

    for mul1 in rmulrange:
        for mul2 in rmulrange:
            product = mul1 * mul2
            if IsNumberPalindromic(product):
                return product
    return -1

digitStart = 1
digitStop  = 6
for digitCount in range(digitStart, digitStop):
    lpn = FindLargestPalindromicNumber(digitCount)
    if lpn == -1:
        ans = "does not exist"
    else:
        ans = "is " + str(lpn)
    print "The largest palindrome made from the product of two %d-digit numbers %s." % (digitCount, ans)
