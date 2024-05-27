# finding the correct values input and using try-catch block to exempt the invalid inputs.
value = input("Enter the number for the Table: ")
print(f"Multiplication table for {value} is :")

try:
  for i in range(1,11):
    print(f"{int(value)} * {i} = {int(value)*i}")

except Exception as e:
  print(e)
