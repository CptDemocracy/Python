"""
[ref.href] https://projecteuler.net/problem=1
Multiples of 3 and 5.
If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is
23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def func(nums, upperBound):
    mulSet = set()
    for num in nums:
        product = num
        while product < upperBound:
            mulSet.add(product)
            product += num
    return sum(mulSet)

upperBound = 1000
muls = [3, 5]
sm = func([3, 5], 1000)
print "The sum of multiples of %s below %d is equal to %d." % (" and ".join([str(mul) for mul in muls]), 
                                                               upperBound, 
                                                               sm)
