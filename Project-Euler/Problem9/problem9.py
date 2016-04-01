"""
[ref.href] https://projecteuler.net/problem=9

A Pythagorean triplet.

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

found  = False
target = 1000
eps = 1e-6

for b in range(2, target):
    for a in range(1, b):
        c = (a**2 + b**2)**.5
        # we don't really need this check for this problem
        # but the problem clearly states the square root
        # has to be an integer number
        if int(c)**2 != a**2 + b**2:
            continue
        c = int(c)
        if abs(a + b + c - target) < eps:
            found = True
            break
    if found:
        break

if found:
    product = a * b * c
    print "The values of the Pythagorean triplet, for which a + b + c = %d are:" % (target)
    print "a = ", a
    print "b = ", b
    print "c = ", c
    print "The product of a, b, c is equal to", product
else:
    print "The values of the Pythagorean triplet, for which a + b + c = %d were not found" % (target)
