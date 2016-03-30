"""
PSET-2
Paying Debt Off in a Year

Now write a program that calculates the minimum fixed monthly payment 
needed in order pay off a credit card balance within 12 months. By a 
fixed monthly payment, we mean a single number which does not change 
each month, but instead is a constant amount that will be paid each 
month.
In this problem, we will not be dealing with a minimum monthly 
payment rate.
The following variables contain values as described below:

1. balance - the outstanding balance on the credit card
2. annualInterestRate - annual interest rate as a decimal

Assume that the interest is compounded monthly according to the balance
at the end of the month (after the payment for that month is made). The
monthly payment must be a multiple of $10 and is the same for all months.
Notice that it is possible for the balance to become negative using this 
payment scheme, which is okay. A summary of the required math is found
below:

Monthly interest rate = 
  (Annual interest rate) / 12.0
  
Monthly unpaid balance = 
  (Previous balance) - (Minimum fixed monthly payment)
  
Updated balance each month = 
  (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

SUMMARY:

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

def CalcBalIn_FIXED_MM_PAYMENT(balance, annualIntRate, monthlyPayment, MONTHS = 12):
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

def CalcMinFixedMonthlyPayment(balance, annualIntRate):
    endBalance = balance
    minFixedMonthlyPayment = 0
    while endBalance > 0:
        minFixedMonthlyPayment += 10
        endBalance = CalcBalIn_FIXED_MM_PAYMENT(balance, annualIntRate, minFixedMonthlyPayment)
    return minFixedMonthlyPayment
        
def py_main():
    ANS_STR = "Lowest Payment: %d"
    print(ANS_STR % CalcMinFixedMonthlyPayment(balance, annualInterestRate))
    
py_main()
