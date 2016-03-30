"""
PSET-3
Hangman Part 4: The Game/Complex Tests

Now you will implement the function hangman, which takes one parameter 
- the secretWord the user is to guess. This starts up an interactive 
game of Hangman between the user and the computer. Be sure you take 
advantage of the three helper functions, isWordGuessed, getGuessedWord,
and getAvailableLetters, that you've defined in the previous part.

Note that if you choose to use the helper functions isWordGuessed, 
getGuessedWord, or getAvailableLetters, you do not need to paste your 
definitions in the box. We have supplied our implementations of these 
functions for your use in this part of the problem. If you use 
additional helper functions, you will need to paste those definitions 
here.
"""

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    INPUT_MSG_STR = "Please guess a letter: "
    GUESSES_LEFT_STR = "You have {:d} guesses left."
    GOOD_GUESS_STR = "Good guess: {:s}"
    BAD_GUESS_STR = "Oops! That letter is not in my word: {:s}"
    OLD_GUESS_STR = "Oops! You've already guessed that letter: {:s}"
    GAME_LOST_STR = "Sorry, you ran out of guesses. The word was {:s}."
    GAME_WON_STR = "Congratulations, you won!"
    SEPARATOR_STR = "-------------"
    AVAILABLE_CHARS_STR = "Available letters: {:s}"

    def main():
        guessedCharsList = []
        guesses = 8
        
        print "Welcome to the game, Hangman!\nI am \
thinking of a word that is {:d} letters long.".format(len(secretWord))

        while True:
            
            print SEPARATOR_STR
            
            if guesses <= 0:
                print GAME_LOST_STR.format(secretWord)
                return False
            if isWordGuessed(secretWord, guessedCharsList):
                print GAME_WON_STR
                return True
                
            print GUESSES_LEFT_STR.format(guesses)
            print AVAILABLE_CHARS_STR.format(getAvailableLetters(guessedCharsList))
            
            userInput = raw_input(INPUT_MSG_STR).lower()
            guessedWord = getGuessedWord(secretWord, guessedCharsList)

            if userInput in guessedCharsList:
                print OLD_GUESS_STR.format(guessedWord)
            else:
                guessedCharsList.append(userInput)
                if userInput in secretWord:
                    guessedWord = getGuessedWord(secretWord, guessedCharsList)
                    print GOOD_GUESS_STR.format(guessedWord)
                else:
                    guesses -= 1
                    print BAD_GUESS_STR.format(guessedWord)

    main()
