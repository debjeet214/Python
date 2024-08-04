class arithmetic_opt():
  def __init__(self, n1):
    self.n1 = n1
    
  def add(self, n2):
    return self.n1 + n2
  
  def sub(self, n2):
    return self.n1 - n2

  @staticmethod                 # static method
  def mutliple_opt(n1, n2, opt):   
    if opt == '*':
      return n1 * n2
    elif opt == '/':
      return n1 / n2

e1 = arithmetic_opt(10)
print(e1.add(20))
print(e1.sub(20))
print(arithmetic_opt.mutliple_opt(10, 20, '*'))   # can be called using the class name
print(e1.mutliple_opt(10, 20, '*'))               # can be used with instance too
