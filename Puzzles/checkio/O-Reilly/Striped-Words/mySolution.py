VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def isVowel(char):
    return char.lower() in ('a','e','i','o','u','y')

def isAlternating(word):
    if len(word) < 2:
        return False
    if not word[0].isalpha():
        return False
    isLastVowel = isVowel(word[0])
    for i in range(1, len(word)):
        char = word[i]
        if not char.isalpha():
            return False
        isCurrVowel = isVowel(char)
        if not isLastVowel ^ isCurrVowel:
            return False
        isLastVowel = isCurrVowel
    return True

def checkio(sentence):
    words = []
    i = 0
    start = 0
    sentenceLen = len(sentence)
    while True:
        if i >= sentenceLen:
            words.append(sentence[start:sentenceLen])
            break
        if not sentence[i].isalnum():
            words.append(sentence[start:i])
            start = i + 1
        i += 1    
    if len(words) == 0:
        return 0
    count = 0
    for word in words:
        if isAlternating(word):
            count += 1
    return count
