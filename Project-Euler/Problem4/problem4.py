"""
[ref.href] https://projecteuler.net/problem=4

Largest palindrome product.

A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is
9009 = 91 x 99

Find the largest palindrome made from the product of two
3-digit numbers.
"""

def IsPalindrome(n):
    s = str(n)
    return s == "".join(t for t in reversed(s))

def GetLargestPalindromeProduct(maxdigits):
    a = 1 * 10 ** (maxdigits - 1)
    b = 1 * 10 ** maxdigits - 1
    mx = 0
    for m1 in xrange(a, b + 1):
        for m2 in xrange(a, b + 1):
            product = m1 * m2
            if IsPalindrome(product) and product > mx:
                mx = product
    return mx

maxdigits = 3
maxpali = GetLargestPalindromeProduct(maxdigits)
print "The largest palindrome made from the product of two %d-digit numbers is %d." % (maxdigits, maxpali)
