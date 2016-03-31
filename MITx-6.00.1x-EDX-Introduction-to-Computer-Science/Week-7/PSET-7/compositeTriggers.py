"""
PSET-7
Part 2: Triggers (CompositeTriggers)

So the triggers from the previous page are mildly interesting, but 
we want to do better: we want to 'compose' the earlier triggers, 
to set up more powerful alert rules. For instance, we may want to 
raise an alert only when both "google" and "stock" were present in 
the news item (an idea we can't express right now).

Note that these triggers are not word triggers and should not be 
subclasses of WordTrigger.

PROBLEM 6

Implement a NOT trigger (NotTrigger).

This trigger should produce its output by inverting the output of 
another trigger. The NOT trigger should take this other trigger as
an argument to its constructor. (Why its constructor? Because we 
can't change what parameters evaluate takes in... that'd break our 
polymorphism). So, given a trigger T and a news item x, the output 
of the NOT trigger's evaluate method should be equivalent to not
T.evaluate(x).

PROBLEM 7

Implement an AND trigger (AndTrigger).

This trigger should take two triggers as arguments to its constructor, 
and should fire on a news story only if both of the inputted triggers
would fire on that item.

PROBLEM 8

Implement an OR trigger (OrTrigger).

This trigger should take two triggers as arguments to its constructor,
and should fire if either one (or both) of its inputted triggers would
fire on that item.
"""

# Enter your code for WordTrigger, TitleTrigger,
# NotTrigger, AndTrigger, and OrTrigger in this box

class WordTrigger(Trigger):      
    def __init__(self, word):
        self.word = word

    def internalAreCharsEqualIgnoreCase(self, c1, c2):
        if type(c1) != str or type(c2) != str:
            raise TypeError("Arg not of type str")
        if len(c1) > 1 or len(c2) > 1:
            raise TypeError("Expected a char. Length not equal to 1")
        return c1[0] == c2[0] or \
               (ord(c1[0]) > 0x60 and (ord(c1[0]) - 0x20 == ord(c2[0])) or ord(c1[0]) < 0x5A and (ord(c1[0]) + 0x20 == ord(c2[0])))
    
    def isWordIn(self, text):
        """
        Returns True if word is present in text as
        whole word. False otherwise.
        """
        charsMatched = 0
        
        firstCharMatchInd = -1
        for i in range( len(text) ):
            
            if self.internalAreCharsEqualIgnoreCase(text[i], self.word[0]):
            # case-insensitive check for text[i] == self.word[0]
                firstCharMatchInd = i
                charsMatched += 1

                wordInd = 1
                while wordInd < len(self.word) and wordInd + firstCharMatchInd < len(text):
                    if self.internalAreCharsEqualIgnoreCase(self.word[wordInd], text[wordInd + firstCharMatchInd]):
                    # case-insensitive check for self.word[wordInd] == text[wordInd + firstCharMatchInd]
                        charsMatched += 1
                        wordInd += 1
                    elif self.internalAreCharsEqualIgnoreCase(self.word[wordInd], self.word[0]):
                    # case-insensitive check for text[i] == self.word[0]
                        charsMatched = 1
                        firstCharMatchInd = wordInd + firstCharMatchInd
                        wordInd = firstCharMatchInd
                        continue
                    else:
                        charsMatched = 0
                        i = wordInd + firstCharMatchInd
                        break
                    
                if charsMatched == len(self.word):
                    if len(self.word) == len(text):
                        return True
                    elif firstCharMatchInd > 0 and firstCharMatchInd + len(self.word) == len(text):
                        if text[firstCharMatchInd - 1].isspace() or text[firstCharMatchInd - 1] in string.punctuation:
                            return True
                    elif firstCharMatchInd == 0 and firstCharMatchInd + len(self.word) + 1 < len(text):
                        if text[firstCharMatchInd + len(self.word)].isspace() or text[firstCharMatchInd + len(self.word)] in string.punctuation:
                            return True
                    else:
                        if (text[firstCharMatchInd - 1].isspace() or text[firstCharMatchInd - 1] in string.punctuation) \
                           and (text[firstCharMatchInd + len(self.word)].isspace() or text[firstCharMatchInd + len(self.word)] in string.punctuation):
                            return True
        return False        

class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.isWordIn( story.getTitle() )

class NotTrigger(Trigger):
    def __init__(self, T):
        self.T = T

    def evaluate(self, story):
        return not self.T.evaluate(story)
    
class AndTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        return self.T1.evaluate(story) and self.T2.evaluate(story)
    
class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        return self.T1.evaluate(story) or self.T2.evaluate(story)
