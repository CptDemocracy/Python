"""
Quiz Problem 8

Write a Python function called satisfiesF that has the specification 
below. Then make the function call run_satisfiesF(L, satisfiesF). 
Your code should look like:

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # Your function implementation here

run_satisfiesF(L, satisfiesF)

For your own testing of satisfiesF, for example, the following test 
function f and test code:

  def f(s):
      return 'a' in s
        
  L = ['a', 'b', 'a']
  print satisfiesF(L)
  print L

Should print:

  2
  ['a', 'a']

Do not define f or run_satisfiesF. Do not leave any debugging print 
statements.

"""

def satisfiesF(L):

    def rem(L, remAtIndList):
        for i in range(0, len(remAtIndList)):
            L.pop(remAtIndList[i])
            for j in range(i, len(remAtIndList)):
                remAtIndList[j] -= 1
    
    indUnsatisfactL = []
    for i in range(0, len(L)):
        if f(L[i]) == False:
            indUnsatisfactL.append(i)
    rem(L, indUnsatisfactL)
    return len(L)

run_satisfiesF(L, satisfiesF)
