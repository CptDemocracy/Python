"""
PSET-6

Your friend, who is also taking 6.00.1x, is really excited about the program she
wrote for Problem 1 of this problem set. She sends you emails, but they're all 
encrypted with the Caesar cipher!

If you know which shift key she is using, then decrypting her message is an easy
task. If the string message is the encrypted message and k is the shift key she
is using, then calling applyShift(message, 26-k) returns her original message. 
Do you see why?

The problem is, you don't know which shift key she is using. The good news is, 
you know your friend only speaks and writes English words. So if you can write 
a program to find the decoding that produces the maximum number of real English
words, you can probably find the right decoding (there's always a chance that 
the shift may not be unique. Accounting for this would use statistical methods
that we won't require of you.)

Implement findBestShift(). This function takes a wordList and a sample of 
encrypted text and attempts to find the shift that encoded the text. A simple 
indication of whether or not the correct shift has been found is if most of 
the words obtained after a shift are valid words. Note that this only means that
most of the words obtained are actual words. It is possible to have a message 
that can be decoded by two separate shifts into different sets of words. While 
there are various strategies for deciding between ambiguous decryptions, for 
this problem we are only looking for a simple solution.

To assist you in solving this problem, we have provided a helper function, 
isWord(wordList, word). This simply determines if word is a valid word according
to the wordList. This function ignores capitalization and punctuation.
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

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    def linearFind(wordList, words):
        if len(words) == 0:
            raise ValueError("empty text")
        alpha_len = 26
        matches = 0
        mismatches = 0
        for k in range(alpha_len):
            if matches > mismatches:
                return (alpha_len - (k - 1)) % alpha_len

            matches = 0
            mismatches = 0
            for word in words:
                word = strip(word.lower())
                enc = applyCoder_CSTR(word, alpha_len - k)
                if enc in wordList:
                    matches += 1
                else:
                    mismatches += 1
        return 0

    def randTestFind(wordList, words):
        if len(words) == 0:
            raise ValueError("empty text")
        alpha_len = 26
        iters = 5
        found = False
        if iters >= len(words):
            iters = len(words) - 1
        for k in range(alpha_len):
            if found == True:
                return (alpha_len - (k - 1)) % alpha_len
            """
            Creating history for random indices
            to avoid the same word being tested
            more than once.
            """
            rands = []
            
            for i in range(iters):
                rand = random.randint(0, len(words) - 1)
                while rand in rands:
                    rand = random.randint(0, len(words) - 1)
                rands.append(rand)
                word = strip(words[rand].lower())
                enc  = applyCoder_CSTR(word, alpha_len - k)
                if enc in wordList:
                    found = True
                else:
                    found = False
        return 0
    
    ####----findBestShift----####
    if text == "":
        raise ValueError("empty text")
    LINEAR_TO_RAND_SEARCH_THRESHOLD = 15
    words = text.split()
    if len(words) < LINEAR_TO_RAND_SEARCH_THRESHOLD:
        return linearFind(wordList, words)
    return randTestFind(wordList, words)
    

def strip(word, pred = lambda char: char.isalpha()):
    newWord = ""
    for char in word:
        if pred(char):
            newWord += char
    return newWord
