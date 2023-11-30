import math


class Circle:
    def __init__(self):
        self.radius = float()

    def parameter(self):
        return self.radius * 2 * math.pi

    def area(self):
        return self.radius ** 2 * math.pi


class Ellipse:
    def __init__(self):
        self.major_axis = float()
        self.minor_axis = float()

    def perimeter(self):
        pass

    def area(self):
        pass