"""
[ref.href] leetcode.com/problems/valid-parentheses
"
  Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
  
  The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opparens = {
            '(':')',
            '[':']',
            '{':'}' 
            }
        clparens = {
            ')':'(',
            ']':'[',
            '}':'{'
            }
        try:
            for c in s:
                if c in opparens:
                    stack.append(c)
                elif c in clparens:
                    if stack[-1] == clparens[c]:
                        stack.pop()
                    else: 
                        return False
        except IndexError:
            return False
        return len(stack) == 0
                
            
