class person:
  name = "Mitali"
  age = 20
  gender = "male"
  job = "accountant"
  def pronoun(self): # Add self to access class attributes
    if self.gender == "female" or self.gender == "Female": # Use self.gender
      pronoun = "She" 
    elif self.gender == "male" or self.gender == "Male":
      pronoun = "he"
    return pronoun

  def show(self):
    # Call pronoun as a method of the class
    print(f"{self.name}'s age is {self.age}. {self.pronoun()} is {self.gender} who works as an {self.job}") 
    # Remove gender argument, call method directly

a = person()
a.show()

b = person()
b.name = "Nikita"
b.age = 22
b.gender = "female"
b.job = "teacher"
b.show()
