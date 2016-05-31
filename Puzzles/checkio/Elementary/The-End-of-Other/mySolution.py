def checkio(word_set):
    if len(word_set) < 2:
        return False
   
    for word in word_set:
        for i in range(len(word)):
            other_word_set_set = word_set - {word}
            if word[i:] in other_word_set_set:
                return True
    return False
