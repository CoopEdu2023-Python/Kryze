class Student:

    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade

    def __len__(self):
        return len(self.name)


stu1 = Student(1, "Kryze", 10)
stu2 = Student(2, "Van", 12)
print(len(stu1), len(stu2))