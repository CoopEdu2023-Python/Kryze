class Student:

    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade

    def __del__(self):
        print(f"student {self.name} has been deleted")


stu1 = Student(1, "Kryze", 10)
stu2 = Student(2, "Van", 12)
del stu1
del stu2
