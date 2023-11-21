class Base:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def __str__(self):
        return 'foo'

    def __foo__(self):
        print('Base')

    def __foo(self):
        print(self)

    def test(self):
        self.__foo()


s = Base()
s.test() 