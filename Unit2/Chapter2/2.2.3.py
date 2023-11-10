class Student:

    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade

    def __str__(self):
        return self.name


stu1 = Student(1, "Kryze", 10)
stu2 = Student(2, "Van", 12)
print(stu1, stu2)