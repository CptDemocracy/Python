import math

def simple_areas(*args):
    argc = len(args)
    area = 0.0
    ROUND_TO_DIGS = 2
    if argc == 1:
        # Circle
        rad = args[0] / 2.0
        area = math.pi * rad ** 2
    elif argc == 2:
        # Rectangle
        a, b = args[0], args[1]
        area = a * b
    elif argc == 3:
        # Triangle
        a, b, c = args[0], args[1], args[2]
        half_perim = (a + b + c) / 2.0
        area = math.sqrt(half_perim * (half_perim - a) * (half_perim - b) * (half_perim - c))
    else:
        raise ValueError("there must be at least one argument to this function and at most 3")
    return round(area, ROUND_TO_DIGS)
