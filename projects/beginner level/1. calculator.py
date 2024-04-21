print("hi python is working")

num1 = float(input("Enteer the first Number: "))
num2 = float(input("Enteer the second Number: "))

operator = input("Enter '+' if want to add two numbers \nEnter '-' if you want to substract \nEnter '*' if you wannt multiply \nEnter '/' for division : ")

if(operator == '+'):
  print(num1+num2)
elif(operator == '-'):
  print(num1-num2)
elif(operator == '*'):
  print(num1*num2)
elif(operator == '/'):
  print(num1/num2)
else:
  print("enter a correct calculation sign: ")
