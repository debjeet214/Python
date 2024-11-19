# simple interest

def simple_int(p, n, r):
  print("The principle amount is:", p)
  print("The time period is:", n)
  print("The rate of interest is:", r)
  si = (p * n * r)/100
  print("The simple interest is:", si)

simple_int(25000, 10, 12)
