import math

def checkio(a, b, c):
    angles = [0, 0, 0]

    # check if valid triangle
    if a + b <= c:
        return angles
    if a + c <= b:
        return angles
    if b + c <= a:
        return angles
    
    angles[0] = int(round((math.degrees(math.acos((b**2 + c**2 - a**2) / (2.0 * b * c))))))
    angles[1] = int(round((math.degrees(math.acos((a**2 + c**2 - b**2) / (2.0 * a * c))))))
    angles[2] = 180 - (angles[0] + angles[1])
    angles.sort()
    return angles
