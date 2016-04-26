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

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
