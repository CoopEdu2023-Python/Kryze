class A:
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self):
        super().__init__(self)