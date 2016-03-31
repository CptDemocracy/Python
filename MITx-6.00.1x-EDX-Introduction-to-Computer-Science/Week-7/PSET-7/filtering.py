"""
PSET-7
Part 3: Filtering

At this point, you can run ps7.py, and it will fetch and display Google 
and Yahoo news items for you in little pop-up windows. How many news 
items? All of them.

Right now, the code we've given you in ps7.py gets all of the feeds 
every minute, and displays the result. This is nice, but, remember, 
the goal here was to filter out only the the stories we wanted.

PROBLEM 10

Write a function, filterStories(stories, triggerlist) that takes in 
a list of news stories and a list of triggers, and returns a list of 
only the stories for which any of the triggers fires on. The list of 
stories should be unique - that is, do not include any duplicates in 
the list. For example, if 2 triggers fire on StoryA, only include 
StoryA in the list one time.
"""

# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, PhraseTrigger, and 
# filterStories in this box

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


def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """

    # triggerlist arg is a list of objects of type Trigger
    # stories arg is a list of objects of type NewsStory

    storiesFiredOnList = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                storiesFiredOnList.append(story)
                break    
    return storiesFiredOnList
