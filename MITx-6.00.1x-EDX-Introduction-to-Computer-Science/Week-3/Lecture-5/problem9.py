"""
Problem 9.

A semordnilap is a word or a phrase that spells a different word when 
backwards ("semordnilap" is a semordnilap of "palindromes"). Here are 
some examples:

  nametag / gateman
  live / evil
  desserts / stressed

Write a recursive program, semordnilap, that takes in two words and 
says if they are semordnilap.
"""

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) != len(str2):
        return False
    if len(str1) == 2:
        if str1[0] == str2[-1]:
            return True
        else:
            return False
    return semordnilap(str1[1:], str2[:-1])
