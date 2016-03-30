"""
PSET-4
Word Game Part 5: Playing a Hand
"""

def isWordLenValid(word, n):
    return len(word) <= n

def getWordScore_FIXED(word, n, firstTurn):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    WHOLE_HAND_USED_BONUS_PTS = 50
    
    score = 0
    if isWordLenValid(word, n):
        for char in word:
            score += SCRABBLE_LETTER_VALUES[ char.lower() ]
        score *= len(word)
        if len(word) == n and firstTurn:
            score += WHOLE_HAND_USED_BONUS_PTS
    return score
    
def playHand(hand, wordList, n):

    ENTER_WORD_PROMPT_STR = "Enter word, or a \".\" to indicate that you are finished: "
    WORD_EARNED_POINTS_STR = "\"{:s}\" earned {:d} points. Total: {:d} points"
    GAME_QUIT_STR = "Goodbye! Total score: {:d} points."
    INVALID_WORD_STR = "Invalid word, please try again."
    OUT_OF_LETTERS_STR = "Run out of letters. Total score: {:d} points."
    CURRENT_HAND_STR = "Current Hand: "

    firstTurn  = True
    totalScore = 0
    while n > 0:
        print(CURRENT_HAND_STR),
        displayHand(hand)
        userInput = raw_input(ENTER_WORD_PROMPT_STR)
        if userInput == '.':
            break
        else:
            if isValidWord(userInput, hand, wordList):
                wordScore = getWordScore_FIXED(userInput, n, firstTurn)
                totalScore += wordScore
                print(WORD_EARNED_POINTS_STR.format(userInput, wordScore, totalScore))
                hand = updateHand(hand, userInput)
                n = calculateHandlen(hand)
                firstTurn = False
            else:
                print(INVALID_WORD_STR)
            print
    if n == 0:
        print(OUT_OF_LETTERS_STR.format(totalScore))
    else:
        print(GAME_QUIT_STR.format(totalScore))
