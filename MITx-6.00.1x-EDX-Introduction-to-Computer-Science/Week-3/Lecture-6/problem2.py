"""
Problem 2.

Write a procedure called oddTuples, which takes a tuple as input, and 
returns a new tuple as output, where every other element of the input 
tuple is copied, starting with the first one. So if test is the tuple 
('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this 
input would return the tuple ('I', 'a', 'tuple').
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    bTup = ()
    for i in range(0, len(aTup)):
        if i == 0 or (i + 1) % 2 != 0:
            bTup += (aTup[i],)
    return bTup
