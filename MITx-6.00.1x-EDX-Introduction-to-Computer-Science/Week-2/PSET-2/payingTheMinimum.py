"""
PSET-2
Paying the Minimum

Write a program to calculate the credit card balance after one year 
if a person only pays the minimum monthly payment required by the 
credit card company each month.

The following variables contain values as described below:

1. balance - the outstanding balance on the credit card
2. annualInterestRate - annual interest rate as a decimal
3. monthlyPaymentRate - minimum monthly payment rate as a decimal

A summary of the required math is found below:

Monthly interest rate      = 
  (Annual interest rate) / 12.0
  
Minimum monthly payment    = 
  (Minimum monthly payment rate) x (Previous balance)
  
Monthly unpaid balance     = 
  (Previous balance) - (Minimum monthly payment)
  
Updated balance each month = 
  (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
  
"""

def calculateUnpaidBalance(balance, monthlyPayment):
    return balance - monthlyPayment

def calculateNextMonthBalance(unpaidBalance, annualInterestRate, months):
    return unpaidBalance + calculateInterest(unpaidBalance, annualInterestRate, months)

def calculateInterest(unpaidBalance, annualInterestRate, months):
    return annualInterestRate / months * unpaidBalance

def calculateMinimumMonthlyPayment(balance, minimumMonthlyPaymentRate):
    return balance * minimumMonthlyPaymentRate

def isMonthlyPaymentSufficient(payment, balance, minimumMonthlyPaymentRate):
    return payment >= calculateMinimumMonthlyPayment(balance, minimumMonthlyPaymentRate)

def calculateCreditCardBalanceIn(balance, annualInterestRate, minimumMonthlyPaymentRate, \
                                 months = 12, outputToConsole = True, decPlaces = 2):
    if outputToConsole:
        FORMAT_STR = "Month: {:d}\nMinimum monthly payment: {:." + str(decPlaces)+ "f}\n" +\
                     "Remaining balance: {:." + str(decPlaces)+ "f}"

    month = 0
    totalPaid = 0
    minMonthlyPayment = calculateMinimumMonthlyPayment(balance, minimumMonthlyPaymentRate)
    unpaidBalance = calculateUnpaidBalance(balance, minMonthlyPayment)
    while month <= months:
        if month > 0 and outputToConsole:
            print(FORMAT_STR.format(month, minMonthlyPayment, balance))
        if month == months:
            break
        minMonthlyPayment = calculateMinimumMonthlyPayment(balance, minimumMonthlyPaymentRate)
        totalPaid += minMonthlyPayment
        unpaidBalance = calculateUnpaidBalance(balance, minMonthlyPayment)
        balance = calculateNextMonthBalance(unpaidBalance, annualInterestRate, months)
        month +=1
    if outputToConsole:
        print(("Total paid: {:." + str(decPlaces) + "f}").format(totalPaid))
        print(("Remaining balance: {:." + str(decPlaces)+ "f}").format(balance))
    return balance


def py_main():
    months = 12
    calculateCreditCardBalanceIn(balance, annualInterestRate, monthlyPaymentRate, months)

py_main()
