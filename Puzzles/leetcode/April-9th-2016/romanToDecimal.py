"""
  [ref.href] leetcode.com/problems/roman-to-integer
  
  "
    Given a roman numeral, convert it to an integer.
    
    Input is guaranteed to be within the range from 1 to 3999.
  "
"""

class Solution(object):
    def romanToInt(self, s): 
        nums = { 'I': 1,  'V': 5,   'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 
                 'M': 1000 }
        ln = len(s)
        value = 0
        i = 0
        while i < ln:
            currval = nums[s[i].upper()]
            if i == ln - 1:
                next = currval
            else:
                next = nums[s[i + 1].upper()]
            if currval < next:
                value -= currval
                while (i > 0 
                       and currval < next 
                       and currval > nums[s[i - 1].upper()]):
                    value -= currval
            else:
                value += currval
            i += 1
        return value
