"""
PSET-6
Problem 2: Decryption (decryptStory)

Now that you have all the pieces to the puzzle, please use them to 
decode the file story.txt. In the skeleton file, you will see a method
getStoryString() that will return the encrypted version of the story.
Fill in the following function; it should create the wordList, obtain
the story, and then decrypt the story. Be sure you've read through 
the whole file to see what helper functions we've defined for you that
may assist you in these tasks! This function will be only a few lines
of code (our solution does it in 4 lines).
"""

import string
import random
import operator

# helper classes code
# --------------------------------

class CharAlphaASCII(object):

    ALPHA_LEN = 26
    ASCII_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ASCII_CHARS_IND = {'A': 0, 'C': 2, 'B': 1, 'E': 4, 'D': 3, 'G': 6, 'F': 5, \
                       'I': 8, 'H': 7, 'K': 10, 'J': 9, 'M': 12, 'L': 11, \
                       'O': 14, 'N': 13, 'Q': 16, 'P': 15, 'S': 18, 'R': 17, \
                       'U': 20, 'T': 19, 'W': 22, 'V': 21, 'Y': 24, 'X': 23, \
                       'Z': 25, \
                       'a': 26, 'c': 28, 'b': 27, 'e': 30, 'd': 29, 'g': 32, \
                       'f': 31, 'i': 34, 'h': 33, 'k': 36, 'j': 35, 'm': 38, \
                       'l': 37, 'o': 40, 'n': 39, 'q': 42, 'p': 41, 's': 44, \
                       'r': 43, 'u': 46, 't': 45, 'w': 48, 'v': 47, 'y': 50, \
                       'x': 49, 'z': 51}
    
    def __init__(self, char):
        if len(char) > 1:
            raise ValueError("CharAlphaASCII can't be more than 1 of length")
        if not char.isalpha():
            raise ValueError("CharAlphaASCII only accepts ASCII alpha chars")
        self.char = char[0]

    def __add__(self, num):
        if type(num) != int:
           raise TypeError
        return CharAlphaASCII( self.operation(num, operator.add) )

    def __sub__(self, num):
        if type(num) != int:
           raise TypeError
        return CharAlphaASCII( self.operation(num, operator.sub) )

    def __str__(self):
        return self.char

    def __lt__(self, char):
        return self.char < char

    def __le__(self, char):
        return self.char <= char

    def __eq__(self, char):
        return self.char == char
    
    def __gt__(self, char):
        return self.char > char

    def __ge__(self, char):
        return self.char >= char

    def __len__(self, char):
        return len(self.char)
    
    def operation(self, num, op):
        if type(num) != int:
           raise TypeError
        index = self.ASCII_CHARS_IND[self.char]
        if index < self.ALPHA_LEN:
            newIndex = op(index, num) % self.ALPHA_LEN
        else:
            newIndex = op(index, num) % self.ALPHA_LEN + self.ALPHA_LEN  
        return self.ASCII_CHARS[newIndex]

    def ToUnicode(self):
        return ord(self.char)

class Cstr(str, object):
    def __init__(self, s):
        self.s = s

    def __add__(self, s):
        return Cstr(self.s + str(s))

    def __str__(self):
        return self.s
        
# --------------------------------
# END of helper classes code

def applyCoder_CSTR(text, shift):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    cs = Cstr("")
    for char in text:
        if char.isalpha():
            C = CharAlphaASCII(char)
            C += shift
            cs += C
        else:
            cs += char
    return str(cs)

def decryptStory():
    wordList = loadWords()
    story = getStoryString()
    return applyCoder_CSTR(story, findBestShift(wordList, story))
