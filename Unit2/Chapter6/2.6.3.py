import math


class MathUtils:
    pi = math.pi

    def calculate_square_root(self, number):
        return number ** 0.5

    @classmethod
    def calculate_circle_area(cls, radius):
        return radius ** 2 * cls.pi

    @staticmethod
    def is_prime(number):
        for i in range(number ** 0.5 + 1):
            if number % i == 0:
                return False
        else:
            return True
