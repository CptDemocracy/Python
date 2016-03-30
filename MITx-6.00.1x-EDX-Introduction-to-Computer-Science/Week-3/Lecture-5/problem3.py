"""
Problem 3.

The function recurPower(base, exp) from Problem 2 computed base^exp 
by decomposing the problem into one recursive case and one base case:

  base^exp = base * base^(exp - 1)  if exp > 0
  base^exp = 1                      if exp = 0
  
Another way to solve this problem just using multiplication 
(and remainder) is to note that:

  base^exp = (base^2)^(exp/2)       if exp > 0 and exp is even
  base^exp = base * base^(exp - 1)  if exp > 0 and exp is odd
  base^exp = 1                      if exp = 0

Write a procedure recurPowerNew which recursively computes 
exponentials using this idea.
"""

def sign(n):
    if sign > 0:
        return 1
    elif sign < 0:
        return -1
    else:
        return 0

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1.0
    if exp == 1:
        return base
    expSign = sign(exp)
    if abs(exp) > 1:
        if abs(exp) % 2 == 0:
            if expSign > 0:
                return recurPowerNew(base * base, abs(exp) / 2.0)
            else:
                return 1.0 / (recurPowerNew(base * base, abs(exp) / 2.0))
        elif abs(exp) % 2 == 1:
            if expSign > 0:
                return base * recurPowerNew(base, abs(exp) - 1)
            else:
                return 1.0 / (base * recurPowerNew(base, abs(exp) - 1))
    return -1.0
