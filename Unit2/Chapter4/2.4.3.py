class Test:
    def __init__(self):
        self.id = int()
        self.points = int()

    def scoring(self):
        pass


class Exam(Test):
    def __init__(self):
        super().__init__()
        self.start_time = int()
        self.end_time = int()