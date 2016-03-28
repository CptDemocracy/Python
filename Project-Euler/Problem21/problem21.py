"""
[ref.] https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and 
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

def AreAmicableNumbers(n1, n2):
    divs1 = GetProperDivisorsFor(n1)
    divs2 = GetProperDivisorsFor(n2)
    return sum(divs1) == n2 and sum(divs2) == n1

def GetProperDivisorsFor(n):
    divs = []
    for i in xrange(1, n // 2 + 1):
        if n % i == 0:
            divs.append(i)
    return divs

def GetAmicableNumbersInRange(start, stop):
    anums = []
    anumsSet = set()
    for i in range(start, stop):
        if i not in anumsSet:
            divs1 = GetProperDivisorsFor(i)
            j = sum(divs1)
            divs2 = GetProperDivisorsFor(j)
            if i !=j and sum(divs2) == i:
                anums.append(i)
                anums.append(j)
                anumsSet.add(i)
                anumsSet.add(j)
    return anums

LB = 1
UB = 10000
anums = GetAmicableNumbersInRange(LB, UB)
ans = sum(anums)
print "The sum of all the amicable numbers under %d is equal to %d." % (UB, ans)
