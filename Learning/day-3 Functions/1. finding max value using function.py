def check_max(a, b):
  if(a>b):
    print(a, "is the bigger number ")
  elif(a == b):
    print( " Both the input  numbers are the same")
  else:
    print(b, "is the bigger number")


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

check_max(num1, num2)
