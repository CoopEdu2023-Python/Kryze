class Rectangle:
    total_rectangles = 0

    def __init__(self):
        self.length, self.width = int

    def calculate_area(self):
        return self.length * self.width

    @classmethod
    def get_total_rectangles(cls):
        print(cls.total_rectangles)

    @staticmethod
    def is_square(length, width):
        return length == width != 0