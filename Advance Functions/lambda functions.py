# A lambda function is a small anonymous function defined with the lambda keyword in programming languages like Python. It is used primarily for creating small, one-off functions without needing to formally define a function using the def keyword.
#ex-1
# lambda function

def app(fx, value):
  print(fx(value))

# to create a lambda function by taking function as variable
double = lambda x: x*2
print(double(10))
app(lambda x: x*x, 10)
