class employee:   # parent class
  def __init__(self, name, id, salary):
    self.name = name
    self.id = id
    self.salary = salary

class programmer(employee):    # child class inherited
  def __init__(self, name, id, salary, lang, exp):
    super().__init__(name, id, salary)    # using super keyword to remove dublicate code (DRY)
    self.lang = lang
    self.exp = exp

ranjani = employee("ranjani", 2200, 45000)
debjeet = programmer("Debjeet", 2146, 76000, "Python", 3)

print(debjeet.name)
print(debjeet.id)
print(debjeet.salary)
print(debjeet.lang)
print(debjeet.exp)
