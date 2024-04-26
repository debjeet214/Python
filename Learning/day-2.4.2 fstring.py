name = input("Enter Your name: ")
age = int(input("Enter your age: "))

if(age >= 18):
  print(f"Hello {name}, as you are {age} years old and you are eligible.")
else:
  print(f"Hello {name}, as you are {age} years old and you are not eligible for this post.")

# f string to round up floating values.
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 45.887382))  # this will print only two floatign value after the point
