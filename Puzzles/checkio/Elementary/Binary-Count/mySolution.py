def checkio(num):
    unityCount = 0
    while True:
        if num % 2 == 1:
            unityCount += 1
        num /= 2
        if num == 0:
            break
    return unityCount
