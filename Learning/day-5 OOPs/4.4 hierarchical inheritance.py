# prompt: create hierarchical inheritance where there is the college as base class and department, library, student, employee are the child class

class College:
  def __init__(self, name, location):
    self.name = name
    self.location = location

  def display_info(self):
    print(f"the name of the College is {self.name} which is in {self.location}")

class Department(College):
  def __init__(self, name, location, dept_name, hod):
    super().__init__(name, location)
    self.dept_name = dept_name
    self.hod = hod

  def display_info(self):
    super().display_info()
    print(f"Department: {self.dept_name}")
    print(f"Head of Department: {self.hod}")

class Library(College):
  def __init__(self, name, location, num_books, librarian):
    super().__init__(name, location)
    self.num_books = num_books
    self.librarian = librarian

  def display_info(self):
    super().display_info()
    print(f"Number of Books: {self.num_books}")
    print(f"Librarian: {self.librarian}")

class Student(College):
  def __init__(self, name, location, student_id, major):
    super().__init__(name, location)
    self.student_id = student_id
    self.major = major

  def display_info(self):
    super().display_info()
    print(f"Student ID: {self.student_id}")
    print(f"Major: {self.major}")

class Employee(College):
  def __init__(self, name, location, employee_id, department):
    super().__init__(name, location)
    self.employee_id = employee_id
    self.department = department

  def display_info(self):
    super().display_info()
    print(f"Employee ID: {self.employee_id}")
    print(f"Department: {self.department}")

# Example usage
college = College("ABC College", "New York")
college.display_info()

dept = Department("ABC College", "New York", "Computer Science", "Dr. Smith")
dept.display_info()

library = Library("ABC College", "New York", 10000, "Ms. Jones")
library.display_info()

student = Student("ABC College", "New York", "S12345", "Computer Science")
student.display_info()

employee = Employee("ABC College", "New York", "E67890", "IT")
employee.display_info()
