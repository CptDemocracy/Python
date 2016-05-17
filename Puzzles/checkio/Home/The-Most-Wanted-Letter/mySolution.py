def extractChars(text):
    charsList = []
    for char in text.lower():
        if char not in charsList and unicode.isalpha(char):
            charsList.append(char)
    return charsList
        
def checkio(text):
    text = text.lower()
    chars = extractChars(text)
    C = chars[0]
    C_freq = text.count(C)
    for char in chars:
        if (char < C and text.count(char) == C_freq) or text.count(char) > C_freq:
            C = char
            C_freq = text.count(char)
    return C
