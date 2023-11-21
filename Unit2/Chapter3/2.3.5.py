class Person:
    def __init__(self, name):
        self.__name = name

    def change(self, new_name):
        if len(self.__name) < 10:
            self.__name = new_name


    def __str__(self):
        return self.__name


p = Person("Kryze")
p.change("KryzeZ")
print(p)

