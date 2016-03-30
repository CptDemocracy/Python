"""
PSET-2
Using Bisection Search to Make the Program Faster

You'll notice that in Problem 2, your monthly payment had to be 
a multiple of $10. Why did we make it that way? You can try running 
your code locally so that the payment can be any dollar and cent 
amount (in other words, the monthly payment is a multiple of $0.01). 
Does your code still work? It should, but you may notice that your 
code runs more slowly, especially in cases with very large balances 
and interest rates. (Note: when your code is running on our servers, 
there are limits on the amount of computing time each submission is 
allowed, so your observations from running this experiment on the 
grading system might be limited to an error message complaining 
about too much time taken.)

Well then, how can we calculate a more accurate fixed monthly 
payment than we did in Problem 2 without running into the problem 
of slow code? We can make this program run faster using a technique 
introduced in lecture - bisection search!

The following variables contain values as described below:

  1. balance - the outstanding balance on the credit card
  2. annualInterestRate - annual interest rate as a decimal

SUMMARY 


    - Interest is compounded monthly according to the unpaid balance.
    - Monthly payment is fixed i.e. same for all months.
    - Monthly payment must be a multiple of $10.

    - Monthly interest rate = (Annual interest rate)/12.0<<months>>
    - Monthly unpaid balance = (Balance) - (Monthly payment)
    - Monthly interest = (Monthly interest rate) * (Monthly unpaid balance)
    - Updated monthly balance = (Monthly unpaid balance) +
                                (Monthly interest rate)  * (Monthly unpaid balance)

    Goal: calculate the minimum fixed monthly payment to pay off a balance within 12 months.

    Algorithm:
    1. Calculate unpaid balance.
    2. Calculate interest based on unpaid balance calculated in step 1.
    3. Update balance.
        Updated monthly balance = (Monthly unpaid balance) + (Monthly interest)
"""

def CalcMonthlyIntRate(annualIntRate):
    return annualIntRate / 12.0

def CalcUnpaidBal(monthlyPrevBal, monthlyPayment):
    return monthlyPrevBal - monthlyPayment

def CalcMonthlyInt(monthlyIntRate, monthlyUnpaidBal):
    return monthlyIntRate * monthlyUnpaidBal

def CalcNextMonthBal(monthlyIntRate, monthlyUnpaidBal):
    return monthlyUnpaidBal + CalcMonthlyInt(monthlyIntRate, monthlyUnpaidBal)

def CalcBal_FIXED_MM_PAYMENT(balance, annualIntRate, monthlyPayment, MONTHS = 12):
    MONTHLY_INT_RATE = CalcMonthlyIntRate(annualIntRate)
    
    unpaidBal = CalcUnpaidBal(balance, monthlyPayment)
    interest  = CalcMonthlyInt(MONTHLY_INT_RATE, unpaidBal)

    month = 1
    while month <= MONTHS:
        balance = CalcNextMonthBal(MONTHLY_INT_RATE, unpaidBal)
        if (month == MONTHS):
            break
        unpaidBal = CalcUnpaidBal(balance, monthlyPayment)
        interest  = CalcMonthlyInt(MONTHLY_INT_RATE, unpaidBal)
        month += 1
        
    return balance

def CalcMinFixedMonthlyPayment(balance, annualIntRate, eps = 1e-2):
    lo = balance / 12.0
    hi = (balance * pow(1 + CalcMonthlyIntRate(annualIntRate), 12))/12.0
    midPoint = BiSearch_Find_MidPoint(lo, hi)
    endBalance = CalcBal_FIXED_MM_PAYMENT(balance, annualIntRate, midPoint)
    while abs(endBalance) > eps:
        if midPoint > hi:
            if endBalance > 0:
                hi = midPoint
            else:
                lo = midPoint
        else:
            if endBalance > 0:
                lo = midPoint
            else:
                hi = midPoint
        midPoint = BiSearch_Find_MidPoint(lo, hi)
        endBalance = CalcBal_FIXED_MM_PAYMENT(balance, annualIntRate, midPoint)
    
    return midPoint

def BiSearch(lo, hi, n, eps, CompareToFn):
    midPoint = BiSearch_Find_MidPoint(lo, hi)
    value = CompareToFn(midPoint)
    while abs(n - value) > eps:
        if hi - lo < eps * 1e-1:
            return -1
        if n > value:
            lo = midPoint
        else:
            hi = midPoint         
        midPoint = BiSearch_Find_MidPoint(lo, hi)
        value = CompareToFn(midPoint)

    return midPoint

def BiSearch_Find_MidPoint(lo, hi):
    return (lo + hi) / 2.0

###TESTING FN###
def BiSearch_CompareTo_Fn(midPoint):
    return pow(midPoint, 2)

def BiSearch_Comparer_Fn(value1, value2, eps = 1e-1):
    return abs(value1 - value2) > eps
###END OF TESTING FN###

def py_main():
    decPlaces = 2
    ANS_STR = "Lowest Payment: {:." + str(decPlaces) + "f}"
    print(ANS_STR.format(CalcMinFixedMonthlyPayment(balance, annualInterestRate)))
    
py_main()
