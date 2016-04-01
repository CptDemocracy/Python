"""
[ref.href] https://projecteuler.net/problem=6

Sum square difference.

The sum of the squares of the first ten natural numbers is:

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is:

    3025 - 385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
"""
smallestNaturalNumber = 1
naturalNumberCount = 100
nums = range(smallestNaturalNumber,
             naturalNumberCount + smallestNaturalNumber)
squares = map(lambda x : x ** 2, nums)
sumOfSquares = sum(squares)
squaredSumOfNums = sum(nums) ** 2
diff = squaredSumOfNums - sumOfSquares
print "The difference between the sum of squares of the first %d is %d." % (naturalNumberCount, diff)
