"""
PSET-1
Alphabetical Substrings.

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which 
the letters occur in alphabetical order. For example, if 
s = 'azcbobobegghakl', then your program should print:

  Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, 
if s = 'abcbcd', then your program should print:

  Longest substring in alphabetical order is: abc
  
"""

def isNextInAlphaOrder(charNow, charNext, invertedAlpha = False):
    if not charNow.isalpha() or not charNext.isalpha():
        return False
    
    charNow = charNow.lower()
    charNext = charNext.lower()
    if (invertedAlpha and ord(charNow) >= ord(charNext)) or\
    (not invertedAlpha and ord(charNow) <= ord(charNext)):
        return True
    return False

def findNextSubstrInAlphaOrder(s, start):
    index = start
    i     = start + 1
    count = 1
    ln    = 1
    while (i < len(s)):
        if isNextInAlphaOrder(s[i - 1], s[i]):
            count += 1
        elif count > 1:
            index = i - count
            ln    = count
            break
        i += 1
    if count > 1:
        index = i - count
        ln    = count
    return [ index, ln ]

def longestSubstrInAlphaOrder(s):
    ln = 0
    found  = 0
    maxInd = -1
    maxLn  = 0
    while found + ln < len(s):
        retVal = findNextSubstrInAlphaOrder(s, found + ln)
        found  = retVal[0]
        ln     = retVal[1]
        if ln > maxLn:
            maxInd = found
            maxLn  = ln
        if ln == 0:
            ln = 1
    return s[ maxInd : maxInd + maxLn ]

def py_main():
    ANS_CHAR = "Longest substring in alphabetical order is: %s"
    sub = longestSubstrInAlphaOrder(s)
    print(ANS_CHAR % sub)

py_main() 
