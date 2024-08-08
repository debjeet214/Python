class square:
  def __init__(self, s1):
    self.s1 = s1
  def area(self):
    return self.s1 * self.s1
  def perimeter(self):
    return 4 * self.s1

class rectangle(square):
  def __init__(self, l, b):
    super().__init__(l)
    self.b = b
  def area(self):
    return self.l * self.b
  def perimeter(self):
    return 2 * (self.l + self.b)

class Cube(square):
  def __init__(self, s1):
    super().__init__(s1)
  def area(self):
    return 6 * self.s1 * self.s1
  def volume(self):
    return self.s1 * self.s1 * self.s1

c1 = Cube(4)
print(c1.area())
print(c1.volume())
