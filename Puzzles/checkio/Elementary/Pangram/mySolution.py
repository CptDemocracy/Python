import string

def check_pangram(text):
    if type(text) != str:
        raise TypeError("text expected to be of type str")

    # generate a dictionary
    alphaDict = { }
    for letter in string.ascii_lowercase:
        alphaDict[letter] = 0
    
    # parse text
    for char in text:
        # if it is a letter, it should be in alphaDict
        char = char.lower()
        if char in alphaDict:
            alphaDict[char] += 1
            
    # check if pangram
    for key in alphaDict.keys():
        if alphaDict[key] == 0:
            return False
    return True
