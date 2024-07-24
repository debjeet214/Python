# multiple inheritance
# Multiple inheritance allows a class to inherit properties and methods from multiple parent classes, providing a way to combine functionalities from different sources.

class Student:
    def __init__(self, name, roll_no, gender):
        self.name = name
        self.roll_no = roll_no
        self.gender = gender

    def get_student_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Gender:", self.gender)

class Marks:
    def __init__(self, maths, physics, chemistry):
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

    def get_marks(self):
        print("Maths:", self.maths)
        print("Physics:", self.physics)
        print("Chemistry:", self.chemistry)

class Result(Student, Marks):
    def __init__(self, name, roll_no, gender, maths, physics, chemistry):
        Student.__init__(self, name, roll_no, gender)
        Marks.__init__(self, maths, physics, chemistry)

    def calculate_total(self):
        total_marks = self.maths + self.physics + self.chemistry
        print("Total Marks:", total_marks)

student1 = Result("Alice", 101, "Female", 80, 75, 90)
student1.get_student_details()
student1.get_marks()
student1.calculate_total()
