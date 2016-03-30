"""
PSET-3
Hangman Part 1: Is the Word Guessed

We'll start by writing 3 simple functions that will help us easily code
the Hangman problem. First, implement the function isWordGuessed that 
takes in two parameters - a string, secretWord, and a list of letters,
lettersGuessed. This function returns a boolean - True if secretWord 
has been guessed (ie, all the letters of secretWord are in 
lettersGuessed) and False otherwise.

For this function, you may assume that all the letters in secretWord 
and lettersGuessed are lowercase.
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in range(0, len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            return False
    return True
        
