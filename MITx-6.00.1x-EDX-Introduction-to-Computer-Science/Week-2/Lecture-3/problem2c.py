"""
Write a while loop that sums the values 1 through end, inclusive.
end is a variable that we define for you. So, for example, if we 
define end to be 6, your code should print out the result:

  21
  
which is 1 + 2 + 3 + 4 + 5 + 6.
"""

i = 1
sm = 0
while (i <= end):
    sm += i
    i  += 1
print sm
