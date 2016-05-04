import re

def checkio(pswd, pswdMinLen = 10, pswdMaxLen = 64):
    if type(pswd) is not unicode:
        raise TypeError("pswd must be a unicode string")
    pswdLen = len(pswd)
    if pswdLen < pswdMinLen or pswdLen > pswdMaxLen:
        return False

    regexps = [r"[A-Za-z0-9]+", r".*[A-Z]+.*", r".*[a-z]+.*", r".*[0-9]+.*"]
    for regexp in regexps:
        pattern = re.compile(regexp)
        matcher = pattern.match(pswd)
        if matcher == None:
            return False
            
    return True
