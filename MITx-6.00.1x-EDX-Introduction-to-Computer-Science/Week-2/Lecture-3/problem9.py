"""
Problem 9.

In this problem, you'll create a program that guesses a secret 
number!

The program works as follows: you (the user) thinks of an integer 
between 0 (inclusive) and 100 (not inclusive). The computer makes 
guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret 
number!
"""

def bsearch(value, r, eps = 1e-7):
    '''
    Role: Searches for a value in given range
    and returns its index or -1 if the value
    was not found.
    
    Pre-Condition: r is a sorted range. Value
    is within the range.

    Post-Condition: index of the value in the
    range r is returned or -1 if the value was
    not found.
    '''

    hiIndex = len(r) - 1
    loIndex = 0
    midPointIndex = 0
    
    while abs(value - r[midPointIndex]) > eps:
        midPointIndex = int((loIndex + hiIndex ) / 2)
        if r[midPointIndex] > value:
            hiIndex = midPointIndex
        else:
            loIndex = midPointIndex
            
        if hiIndex - loIndex == 1:
            return -1

    return midPointIndex

def validateInput(userInput, legalValues = []):
    for i in range(0, len(legalValues)):
        if userInput == legalValues[i]:
            return True
    return False

def requestInput(msg = '', validateInputBool = False, legalValues = [], illegalValueMsg = ''):
    s = raw_input(msg)
    if validateInputBool:
        while validateInput(s, legalValues) == False:
            print(illegalValueMsg)
            s = raw_input(msg)
    return s

def guessGame(firstNum = 0, lastNum = 100):
    HI_GUESS_STR = 'h'
    LO_GUESS_STR = 'l'
    CORRECT_GUESS_STR = 'c'
    LEGAL_INPUT_VALS_ARRAY = [ HI_GUESS_STR, LO_GUESS_STR, CORRECT_GUESS_STR]
    GAME_BEGIN_STR = "Please think of a number between " + str(firstNum) + " and " + str(lastNum) + '!'
    IS_MATCH_STR = "Is your secret number %d?"
    PROMPT_STR = "Enter \'" + HI_GUESS_STR + "\' to indicate the guess is too high. Enter \'"\
                            + LO_GUESS_STR + "\' to indicate the guess is too low. Enter \'"\
                            + CORRECT_GUESS_STR + "\' to indicate I guessed correctly."
    INVALID_INPUT_STR = "Sorry, I did not understand your input."
    GAME_OVER_STR = "Game over. Your secret number was: %d"

    r  = range(firstNum, lastNum + 1)
    hi = lastNum
    lo = firstNum

    print(GAME_BEGIN_STR)
    while True:
        # checks if guessed number
        # was not found within range
        if (hi - lo) == 1:
            return -1
        midPoint = (hi + lo) / 2
        
        s = requestInput(msg = IS_MATCH_STR % midPoint + '\n' + PROMPT_STR + ' ', 
                        validateInputBool = True, 
                        legalValues = LEGAL_INPUT_VALS_ARRAY, 
                        illegalValueMsg = INVALID_INPUT_STR)
        if s == CORRECT_GUESS_STR:
            print(GAME_OVER_STR % midPoint)
            return 0
        elif s == LO_GUESS_STR:
            lo = midPoint
        else:
            hi = midPoint   


## initialize game ##
guessGame()
