"""
PSET-7
Part 2: Triggers (WordTriggers)

Given a set of news stories, your program will generate alerts for 
a subset of those stories. Stories with alerts will be displayed 
to the user, and the other stories will be silently discarded. We 
will represent alerting rules as triggers. A trigger is a rule that 
is evaluated over a single news story and may fire to generate an 
alert. For example, a simple trigger could fire for every news story 
whose title contained the word "Microsoft". Another trigger may be 
set up to fire for all news stories where the summary contained the 
word "Boston". Finally, a more specific trigger could be set up to 
fire only when a news story contained both the words "Microsoft" 
and "Boston" in the summary.

"""

# Enter your code for WordTrigger, TitleTrigger, 
# SubjectTrigger, and SummaryTrigger in this box

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
        
