"""
PSET-7
Part 2: Triggers (PhraseTriggers)

At this point, you have no way of writing a trigger that matches on 
"New York City" -- the only triggers you know how to write would be 
a trigger that would fire on "New" AND "York" AND "City" -- which 
also fires on the phrase "New students at York University love the 
city". It's time to fix this. Since here you're asking for an exact 
match, we will require that the cases match, but we'll be a little 
more flexible on word matching. So, "New York City" will match:

* New York City sees movie premiere
* In the heart of New York City's famous cafe
* New York Cityrandomtexttoproveapointhere

but will not match:

* I love new york city
* I love    New                 York                  City!!!!!!!!!!!!!!

PROBLEM 9

Implement a phrase trigger (PhraseTrigger) that fires when a given 
phrase is in any of the story's subject, title, or summary. The 
phrase should be an argument to the class's constructor.
"""

# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, and PhraseTrigger in this box

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

class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.isWordIn( story.getSubject() )

class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.isWordIn( story.getSummary() )

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.word = phrase

    def isWordIn(self, text):
        charsMatched = 0      
        firstCharMatchInd = -1
        for i in range( len(text) ):
            
            if text[i] == self.word[0]:
                firstCharMatchInd = i
                charsMatched += 1

                wordInd = 1
                while wordInd < len(self.word) and wordInd + firstCharMatchInd < len(text):
                    if self.word[wordInd] == text[wordInd + firstCharMatchInd]:
                        charsMatched += 1
                        wordInd += 1
                    elif self.word[wordInd] == self.word[0]:
                        charsMatched = 1
                        firstCharMatchInd = wordInd + firstCharMatchInd
                        wordInd = firstCharMatchInd
                        continue
                    else:
                        charsMatched = 0
                        i = wordInd + firstCharMatchInd
                        break
                    
                if charsMatched == len(self.word):
                        return True          
        return False

    def evaluate(self, story):
        return self.isWordIn( story.getTitle() ) or \
               self.isWordIn( story.getSubject() ) or \
               self.isWordIn( story.getSummary() )
