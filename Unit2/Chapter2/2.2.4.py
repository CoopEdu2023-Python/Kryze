class Student:

    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade

    def __le__(self, other):
        return self.grade <= other.grade

    def __lt__(self, other):
        return self.grade < other.grade


stu1 = Student(1, "Kryze", 10)
stu2 = Student(2, "Van", 12)
print(stu1 < stu2)
print(stu1 > stu2)
print(stu1 <= stu2)