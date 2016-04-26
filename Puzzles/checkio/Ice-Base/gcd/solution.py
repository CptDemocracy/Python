# The Eucledian gcd algorithm
def greatest_common_divisor(*args):
    argc = len(args)
    if argc < 2:
        return 1
    n, m = args[0], args[1]
    while m > 0:
        temp = m
        m = n % m
        n = temp
    if argc == 2:
        return n
    return greatest_common_divisor(*args[2:] + (n,))
