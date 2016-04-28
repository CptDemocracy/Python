ON        = '-'
OFF       = '.'
ON_BIT    = '1'
OFF_BIT   = '0'
SEPARATOR = ':'

def dec_to_bin(num):
    bits = []
    while True:
        bits.append(str(num % 2))
        num //= 2
        if num == 0:
            break
    bits.reverse()
    return "".join(bits)

def checkio(timestring):    
    hh, mm, ss = timestring.split(SEPARATOR)
    return (' ' + SEPARATOR + ' ').join([hour_to_morse(hh), minute_to_morse(mm), second_to_morse(ss)])    

def second_to_morse(second):
    return timeval_to_morse(second, 3, 4)

def minute_to_morse(minute):
    return timeval_to_morse(minute, 3, 4)

def hour_to_morse(hour):
    return timeval_to_morse(hour, 2, 4)

def timeval_to_morse(timeval, firstDigitMaxBits, secondDigitMaxBits):
    if len(timeval) < 2:
        digit_one_bits = '0'.zfill(firstDigitMaxBits) 
        digit_two_bits  = dec_to_bin(int(timeval[0])).zfill(secondDigitMaxBits)
    else:    
        digit_one_bits = dec_to_bin(int(timeval[0])).zfill(firstDigitMaxBits)
        digit_two_bits  = dec_to_bin(int(timeval[1])).zfill(secondDigitMaxBits)
    digit_one_morse = []
    digit_two_morse = []
    for i in range(firstDigitMaxBits):
        if digit_one_bits[i] == OFF_BIT:
            digit_one_morse.append(OFF)
        else:
            digit_one_morse.append(ON)
    for i in range(secondDigitMaxBits):
        if digit_two_bits[i] == OFF_BIT:
            digit_two_morse.append(OFF)
        else:
            digit_two_morse.append(ON)
    return " ".join(["".join(digit_one_morse), "".join(digit_two_morse)])
