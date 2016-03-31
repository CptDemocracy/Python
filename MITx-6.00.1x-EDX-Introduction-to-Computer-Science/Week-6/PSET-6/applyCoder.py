"""
PSET-6
Problem 1: Encryption (applyCoder)
"""

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    s = ""
    for char in text:
        if char in coder:
            s += coder[char]
        else:
            s += char
    return s
