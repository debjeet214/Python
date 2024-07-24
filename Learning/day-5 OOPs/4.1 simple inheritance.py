# single inheritance
# Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code. 

# here class techers can access the features of the class Employee

class Employee:
    def __init__(self, name, id, city, salary):
        self.name = name
        self.id = id
        self.city = city
        self.salary = salary
    
    def display(self):
        print(f"the employee name of employer {self.id} is {self.name}. he got the salary of {self.salary}")

class teachers(Employee):
  def teaching(self, subject):
    self.subject = subject
    print(f"the teacher {self.name} is teaching {self.subject}")


emp1 = Employee("Jin Hyan", 203, "Seoul", 70000)
emp1.display()

emp2 = Employee("Taeyong", 221, "Seoul", 100000)
emp2.display()

emp3 = teachers("Debjeet Ghosh", 154, "Seoul", 85000)
emp3.teaching("Math")
emp3.display()
