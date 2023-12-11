class Car:
    total_cars = 0

    def __init__(self):
        self.color = None

    def drive(self):
        print("The car is driving")

    @classmethod
    def get_total_cars(cls):
        print(cls.total_cars)

    @staticmethod
    def is_color_valid(color):
        return type(color) == str


car = Car()
Car.total_cars += 1
Car.get_total_cars()