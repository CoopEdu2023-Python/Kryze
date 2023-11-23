class A:
    def __init__(self):
        self.X = 1
        self.Y = 2
        self.Z = 3

    def get_X(self):
        print(self.X)


class B(A):
    def get_Y(self):
        print(self.Y)


class C(B):
    def get_Z(self):
        print(self.Z)


a = A()
b = B()
c = C()
#a: get_X()
#b: get_X()   get_Y()
#c: get_X()   get_Y()    get_Z()