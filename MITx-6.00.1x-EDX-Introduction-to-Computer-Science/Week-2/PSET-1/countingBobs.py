"""
PSET-1
Counting Bobs

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' 
occurs in s. For example, if s = 'azcbobobegghakl', then your 
program should print:

  Number of times bob occurs is: 2

"""

def countPal(target, pal):
    midPoint     = int(len(pal) / 2)
    searchStatus = 0
    startAt      = 0
    count        = 0
    while searchStatus != -1:
        searchStatus = target.find(pal, startAt)
        if searchStatus == -1:
            break
        else:
            count += 1
        startAt = searchStatus + midPoint
    return count
        
def py_main():
    pal = "bob"
    n = countPal(s, pal)
    ANS_STR = "Number of times %s occurs is: %d"
    print(ANS_STR % (pal, n))
    return 0
    
py_main()
