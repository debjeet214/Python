class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.salary = salary
        self.age = age
        
    @classmethod
    def fromstr(koko, string):
        return koko(string.split("-")[0], int(string.split("-")[1]), int(string.split("-")[2]) )

e1 = Employee("Debjeet", 87000, 19)
print(e1.name)
print(e1.salary)
print(type(e1.salary))

e2 = Employee.fromstr("mitali-56000-20")
print(e2.name)
print(e2.salary)
print(type(e2.salary))
