class student:
    def print_inf(self):
        print(self.name, self.gender, self.age)


stu_1 = student()
stu_2 = student()
stu_1.name = 'stu1'
stu_1.gender = 'boy'
stu_1.age = 16
stu_2.name = 'stu2'
stu_2.gender = 'girl'
stu_2.age = 16
print(stu_1.name, stu_1.gender, stu_1.age)
print(stu_2.name, stu_2.gender, stu_2.age)
stu_1.print_inf()
stu_2.print_inf()