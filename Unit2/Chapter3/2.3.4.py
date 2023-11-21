class Test1:
    def __init__(self):
        self._n1 = 10
        self.__n2 = 10
        self.___n3 = 10

    def ____test(self):
        pass


test = Test1()
print(len(dir(test)))

# 实例属性和方法数量是一样的