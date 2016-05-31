import string

def checkio(numStr, radix):
    if type(numStr) not in (str, unicode):
        raise TypeError("number must be in a string format")
    if type(radix) is not int:
        raise TypeError("radix expected to be an int")
    
    # generate radix dictionary
    radixDict = { }
    alphaIndex = 0
    for i in range(radix):
        if i > 9:
            radixDict[string.ascii_lowercase[alphaIndex]] = i
            alphaIndex += 1
        else:
            radixDict[str(i)] = i
    
    # get the result
    result = 0
    numStrLen = len(numStr)
    for i in reversed(range(numStrLen)):
        digit = numStr[i].lower()
        if digit not in radixDict:
            return -1
        result += radixDict[digit] * pow(radix, numStrLen - 1 - i)
    return result
