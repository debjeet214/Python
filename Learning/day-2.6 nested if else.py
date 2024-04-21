
# nested if else statement :

num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number: "))


if( num1<0 and num2<0 ) :
  print("Both numbers are negative ")
elif(num1 > 0):
  if(num1 <10):
    print("it is a single digit number")
  elif(num1<100):
    print("it is a double digit number")
  else:
    print(" it has more than 2 digits")
else:
  print(" it is equal to zero")

