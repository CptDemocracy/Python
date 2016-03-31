"""
PSET-6
Problem 1: Encryption (buildCoder)
"""

import string

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    allchars = string.ascii_uppercase + string.ascii_lowercase
    alpha_len = 26
    keys = {}
    for i in range(0, len(allchars)):
        if i < alpha_len:
            keys[allchars[i]] = allchars[(i + shift) % alpha_len]
        else:
            keys[allchars[i]] = allchars[(i + shift) % alpha_len + alpha_len]
    return keys
