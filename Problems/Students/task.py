class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = name[0] + last_name + str(birth_year)


my_student = Student(input(), input(), input())
print(my_student.id)
