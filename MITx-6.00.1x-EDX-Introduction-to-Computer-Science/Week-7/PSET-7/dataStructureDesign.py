"""
PSET-7
Part 1: Data Structure Design

"""

class NewsStory(object):

    def __init__(self, guid, title, subject, summary, URLMoreContent):
        self.guid  = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.URLMoreContent = URLMoreContent

    def getGuid(self):
        return self.guid

    def getTitle(self):
        return self.title

    def getSubject(self):
        return self.subject

    def getSummary(self):
        return self.summary

    def getLink(self):
        return self.URLMoreContent
