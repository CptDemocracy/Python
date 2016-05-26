class Building(object):
    def __init__(self, south, west, width_WE, width_NS, height = 10):
        self._south = south
        self._west  = west
        self._width_WE = width_WE
        self._width_NS = width_NS
        self._height = height

    def corners(self):
        return {"north-west": [self._south + self._width_NS, self._west],
                "north-east": [self._south + self._width_NS, self._west + self._width_WE],
                "south-west": [self._south, self._west],
                "south-east": [self._south, self._west + self._width_WE]}

    def area(self):
        return self._width_WE * self._width_NS

    def volume(self):
        return self._width_WE * self._width_NS * self._height

    def __repr__(self):
        return "%s(%g, %g, %g, %g, %g)" % ("Building", self._south, self._west,
        self._width_WE, self._width_NS, self._height)

    def __str__(self):
        return self.__repr__()
