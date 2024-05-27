class AgeError(Exception):
  "Raised when the person's age is less than 18"
  pass

try:
  age = int(input("Enter your age: "))
  if(age<18):
    raise AgeError
except ValueError:
  print("please enter a valid age.")
except AgeError:
  print("You are not eligible to vote")

else:
  print("You are eligible to vote")
