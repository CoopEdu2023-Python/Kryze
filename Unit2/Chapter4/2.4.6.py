class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_info(self):
        print(self.brand, self.color)


class Car(Vehicle):
    def __init__(self, brand, color, seat):
        super().__init__(brand, color)
        self.seat = seat

    def show_info(self):
        print(self.brand, self.color, self.seat)


my_vehicle = Vehicle("BMW", "White")
my_car = Car("BMW", "White", 6)
my_vehicle.show_info()
my_car.show_info()

