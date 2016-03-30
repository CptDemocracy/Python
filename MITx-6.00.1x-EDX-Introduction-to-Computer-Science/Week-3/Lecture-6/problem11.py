"""
Problem 11.

Consider the following sequence of expressions:

  animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
  
  animals['d'] = ['donkey']
  animals['d'].append('dog')
  animals['d'].append('dingo')
  
We want to write some simple procedures that work on dictionaries 
to return information.

This time, write a procedure, called biggest, which returns the 
key corresponding to the entry with the largest number of values 
associated with it. If there is more than one such entry, return 
any one of the matching keys.

Example usage:
  >>> biggest(animals)
  'd'

If there are no values in the dictionary, biggest should return None.
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict) == 0:
        return None
    keysList = aDict.keys()
    mx = len(aDict[keysList[0]])
    mxKey = keysList[0]
    for i in range(1, len(keysList)):
        if len(aDict[keysList[i]]) > mx:
            mx = len(aDict[keysList[i]])
            mxKey = keysList[i]
    return mxKey 
