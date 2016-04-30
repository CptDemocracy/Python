def is_palindrome(text):
    return text == "".join([char for char in reversed(text)])

def longest_palindromic(text):
    text_len = len(text)
    longest_pal_len = 0
    longest_pal = ""
    for i in range(len(text)):
        for j in reversed(range(i, text_len)):
            substr = text[i:j + 1]
            if is_palindrome(substr):
                substrLen = len(substr)
                if substrLen > longest_pal_len:
                    longest_pal = substr
                    longest_pal_len = substrLen
    return longest_pal
