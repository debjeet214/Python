#  Normal Fibonacci series

def fibo(n):
  if n == 1:
    return 0
  if n == 2:
    return 1
  return fibo(n-1) + fibo(n-2)

n = int(input("Enter the no of terms in fibonacci series: "))

for i in range(1, n+1):
  print(fibo(i))



# Fibonacci series using the lambda function

fibo = lambda n: n - 1 if n <= 2 else fibo(n - 1) + fibo(n - 2)
n = int(input("Enter the number of terms in Fibonacci series: ")) # Input from the user
print([fibo(i) for i in range(1, n + 1)]) # Generate and print the series
