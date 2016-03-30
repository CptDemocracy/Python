"""
PSET-4
Word Game Part 7: Computer Chooses a Word

Now that you have completed your word game code, you decide that you 
would like to enable your computer (SkyNet) to play the game (your 
hidden agenda is to prove once and for all that computers are inferior
to human intellect!) In Part B you will make a modification to the 
playHand function from part A that will enable this to happen. The 
idea is that you will be able to compare how you as a user succeed 
in the game compared to the computer's performance.

It is your responsibility to create the function compChooseWord(hand, 
wordList, n). Pseudocode is provided in the file ps4b.py.
"""

import string

def compChooseWord(hand, wordList, n):
    def findNextValidWord(hand, wordList, wordListIndex, n):   
        def find(l, start, cmpFn, *args):
            for i in range( start, len(l) ):
                if cmpFn(l[i], *args):
                    return i
            return -1
        
        alpha = string.ascii_lowercase
        for i in range( len(alpha) ):
            char = alpha[i]
            if char in hand:
                startSearchAt = find(wordList, wordListIndex, str.startswith, char)
                while startSearchAt != -1:
                    word = wordList[startSearchAt]
                    
                    if isValidWord(word, hand, wordList):
                        return startSearchAt
                    startSearchAt = find(wordList, startSearchAt + 1, str.startswith, char)           
        return -1
    
    ### END OF findNextValidWord ###

    def handToString(d):
        s = ""
        for char in d:
            for i in range( d[char] ):
                s += char
        return s

    ### UPPER BOUND CHECK ###
    perfectWord = handToString(hand)
    upperBound = getWordScore(perfectWord, n)
    ### /UPPER BOUND CHECK ###
    
    word = None
    i = findNextValidWord(hand, wordList, 0, n)
    
    if i != -1:
        word  = wordList[i]
        score = getWordScore(word, n)
        ln    = len(word)

    while i != -1:
        newWord  = wordList[i]
        newScore = getWordScore(newWord, n)
            
        if newScore > score:
            word  = newWord
            score = newScore
   
        ### UPPER BOUND CHECK ###
        if score >= upperBound:
            break
        ### /UPPER BOUND CHECK ###
        
        i = findNextValidWord(hand, wordList, i + 1, n)
    return word
