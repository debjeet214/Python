# It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

#When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

name = input("Enter Your name: ")
age = int(input("Enter your age: "))

if(age >= 18):
  print(f"Hello {name}, as you are {age} years old and you are eligible.")
else:
  print(f"Hello {name}, as you are {age} years old and you are not eligible for this post.")

# f string to round up floating values.
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 45.887382))  # this will print only two floatign value after the point
