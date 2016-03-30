"""
PSET-4
Word Game Part 8: Computer Plays a Hand

Now that we have the ability to let the computer choose a word, we 
need to set up a function to allow the computer to play a hand - in 
a manner very similar to Part A's playHand function (get the hint?).

Implement the compPlayHand function. This function should allow the 
computer to play a given hand, using the procedure you just wrote in 
the previous part. This should be very similar to the earlier version 
in which a user selected the word, although deciding when it is done
playing a particular hand will be different.
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

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    CURRENT_HAND_STR = "Current Hand: "
    WORD_EARNED_POINTS_STR = "\"{:s}\" earned {:d} points. Total: {:d} points"
    TOTAL_SCORE_STR = "Total score: {:d} points."
    
    AItotalScore = 0
    AIword  = compChooseWord(hand, wordList, n)
    
    while AIword != None:
        AIscore = getWordScore(AIword, n)
        AItotalScore += AIscore
        
        print( CURRENT_HAND_STR ),
        displayHand(hand)
        print( WORD_EARNED_POINTS_STR.format( AIword, AIscore, AItotalScore ) )
        print

        hand = updateHand(hand, AIword)      
        AIword = compChooseWord(hand, wordList, n)
    if calculateHandlen(hand) != 0:
        print( CURRENT_HAND_STR ),
        displayHand(hand)
    print( TOTAL_SCORE_STR.format( AItotalScore ) )
