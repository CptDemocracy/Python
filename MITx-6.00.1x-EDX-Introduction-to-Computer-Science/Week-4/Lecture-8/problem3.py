"""
Problem 3.

Suppose we rewrite the FancyDivide function to use a helper function.

      
def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]


def SimpleDivide(item, denom):
   return item / denom
      

This code raises a ZeroDivisionError exception for the following call:
  FancyDivide([0, 2, 4], 0)

Your task is to change the definition of SimpleDivide so that the call 
does not raise an exception. When dividing by 0, FancyDivide should 
return a list with all 0 elements. Any other error cases should still 
raise exceptions. You should only handle the ZeroDivisionError.

"""

#define the SimpleDivide function here
def SimpleDivide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0
      
