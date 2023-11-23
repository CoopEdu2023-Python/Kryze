class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def get_perimeter(self):
        return (self.width + self.length) * 2

    def get_area(self):
        return self.width * self.length


my_shape = Shape("Red")
my_rectangle = Rectangle("Red", 10, 5)
print(my_rectangle.get_color())
print(my_rectangle.get_perimeter())
print(my_rectangle.get_area())
