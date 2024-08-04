class employee:
  emp_count=0           # class variable
  company="google"      # class variable & default value
  def __init__(self,name,id,salary):    # defining the function
    self.name=name
    self.id=id
    self.salary=salary
    employee.emp_count+=1               # counting the no. of employee in the class

  def show(self):
    print(f"The employee {self.id} name is {self.name} whose salary is {self.salary}")
    print(f"The number of employee in {self.company} is {self.emp_count}")

emp1 = employee("Debjeet", 21760, 45600)   # defining the first instance
emp2 = employee("Ranjani", 21778, 39000)   # defining next instance
employee.company = "Amazon"                # changing the class variable
# emp2.company = "Wipro"                   # this is changing the variable in instance level.
emp1.show()
emp2.show()
