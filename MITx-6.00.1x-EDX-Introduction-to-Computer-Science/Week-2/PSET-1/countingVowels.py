"""
PSET-1
Counting Vowels

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the 
string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
if s = 'azcbobobegghakl', your program should print:

  Number of vowels: 5
  
"""

def countVowels(s):
    vowels = 'aeiou'
    s = s.lower()
    numOfVowels = 0
    for v in vowels:
        numOfVowels += s.count(v)
    return numOfVowels

def py_main():
    OUTPUT_STR = "Number of vowels: %d"
    numOfVowels = countVowels(s)
    print(OUTPUT_STR % numOfVowels)

py_main()
