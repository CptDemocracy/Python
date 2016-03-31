"""
PSET-4
Word Game Part 9: You and your Computer
"""

PROMPT_STR = "Enter n to deal a new hand, r to replay the last hand, or e to end game: "
NO_REPL_AVAIL_STR = "You have not played a hand yet. Please play a new hand first!"
INVALID_CMD = "Invalid command."
CHOOSE_PLAYER_STR = "Enter u to have yourself play, c to have the computer play: "

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    firstGame = True
    lastHand  = {}

    while True:
        userInput = raw_input(PROMPT_STR)
        if userInput == 'n':
            hand = dealHand(HAND_SIZE)
            lastHand = hand.copy()
            playHand_AI_and_human(hand, wordList, HAND_SIZE)
        elif userInput == 'r':
            if len(lastHand) == 0:
                print(NO_REPL_AVAIL_STR)
            else:
                playHand_AI_and_human(lastHand, wordList, HAND_SIZE)
        elif userInput == 'e':
            break
        else:
            print(INVALID_CMD)            
        print

def playHand_AI_and_human(hand, wordList, n):
    userInput = ""
    while userInput != 'u' and userInput != 'c':
        userInput = raw_input(CHOOSE_PLAYER_STR)
        if userInput == 'u':    
            playHand(hand, wordList, n)
        elif userInput == 'c':
            compPlayHand(hand, wordList, n)
        else:
            print(INVALID_CMD)
