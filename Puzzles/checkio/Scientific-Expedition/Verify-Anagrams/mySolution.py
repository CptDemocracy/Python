def verify_anagrams(first_word, second_word):
    charDict = {}
    for char in first_word:
        if char.isalpha():
            char = char.lower()
            if char not in charDict:
                charDict[char] = 1
            else:
                charDict[char] += 1
    for char in second_word:
        if not char.isalpha():
            continue
        char = char.lower()
        if char not in charDict or charDict[char] <= 0:
            return False
        else:
            charDict[char] -= 1
    for char in charDict:
        if charDict[char] > 0:
            return False
    return True
