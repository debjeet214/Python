class persondet:
    nationality = "Indian"
    def __init__(self, name = "Debjeet",age = 19,gender= "Male"):
        self.name=name
        self.age=age
        self.gender=gender
        self.pronoun = "he" if gender == "male" or "Male" else "she"

    def display(self):
        print(f"{self.name}'s age is {self.age} and {self.pronoun} is a {self.gender}")
        print(f"{self.pronoun} is {self.nationality}")


a = persondet("John",20,"male")
a.nationality = "American"
a.display()

b = persondet("Jenifer",21,"female")
b.display()

c = persondet()
c.display()
