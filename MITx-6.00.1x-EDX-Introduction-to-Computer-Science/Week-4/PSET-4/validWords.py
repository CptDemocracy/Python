"""
PSET-4
Word Game Part 3: Valid Words

At this point, we have written code to generate a random hand and 
display that hand to the user. We can also ask the user for a word 
(Python's raw_input) and score the word (using your getWordScore). 
However, at this point we have not written any code to verify that
a word given by a player obeys the rules of the game. A valid word 
is in the word list; and it is composed entirely of letters from 
the current hand. Implement the isValidWord function.
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    CHAR_NOT_FOUND_IN_HAND = -1
    
    word = word.lower()
    if word not in wordList:
        return False
    for char in word:
        charsInHand = hand.get(char, CHAR_NOT_FOUND_IN_HAND)
        if charsInHand == CHAR_NOT_FOUND_IN_HAND or word.count(char) > charsInHand:
            return False
    return True
