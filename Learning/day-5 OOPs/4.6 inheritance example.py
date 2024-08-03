# inheritence 

class dogs:
  _legcount = 4
  def __init__(self, name):
    self.name = name
  def getlegcount(self):     # getter function
    return self._legcount

  def sound(self):
    print(self.name +" barks")

class petdog(dogs):
  def __init__(self, name):
    super().__init__(name)

  def quality(self, additionalq):
    print(self.name + additionalq)

one = dogs("Blacky")
one.sound()

two = petdog("jennifer")
two.sound()
two.quality(" is the cutest")

three = petdog("chissy")
three.quality(" is a obidient dog and can do blackflip too")
