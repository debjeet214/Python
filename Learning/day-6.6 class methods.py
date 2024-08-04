# In Python, classes are a way to define custom data types that can store data and define functions that can manipulate that data. One type of function that can be defined within a class is called a "method."

# class methods: A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class. Class methods are defined using the "@classmethod" decorator, followed by a function definition. The first argument of the function is always "cls," which represents the class itself.

# Class methods are useful in several situations. For example, you might want to create a factory method that creates instances of your class in a specific way. You could define a class method that creates the instance and returns it to the caller. Another common use case is to provide alternative constructors for your class. This can be useful if you want to create instances of your class in multiple ways, but still have a consistent interface for doing so.

# class method
class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod      # decorator to specify a method as class method
  def changeCompany(cls, newCompany):
    cls.company = newCompany          # here this will change the name of company to new company


e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")      # this willc change the company name as well inside the class permanantly.
e1.show()
print(Employee.company)
