"""
[ref.href] https://projecteuler.net/problem=22

Names scores.

Using names.txt ([ref.href] https://projecteuler.net/project/resources/p022_names.txt), a 46K text file containing 
over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical 
value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

path = "p022_names.txt"
mode = "r"
names = []

try:
    # read names
    namesFile = open(path, mode)
    readCharCount = 1
    nameChars = []
    while True: 
        char = namesFile.read(readCharCount)
        byteCount = len(char)
        if byteCount < readCharCount:
            # prevent loitering
            nameChars = []
            break
        if char.isalpha():
            nameChars.append(char)
        elif len(nameChars) > 0:
            name = "".join(nameChars)
            names.append(name)
            nameChars = []
    namesFile.close()

    # sort names
    names.sort()

    # calculate scores, find the sum
    scoresum = 0
    i = 1
    for name in names:
        # calculate score
        score = 0
        for char in name:
            # we know the character is already in uppercase
            # but we invoke str.upper() method as a good
            # programming practice
            score += ord(char.upper()) - ord('A') + 1
        score = score * i
        scoresum += score
        i += 1
    
    # sum the scores
    print "The total sum of name scores in the file is %d." % scoresum

except IOError as e:
    print "File \"%s\" not found." % path
    print e
