# Strings are immutable
a = "!!!Harry!! dO YoU know, debjeet? debjeet !!!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))     # this will strip ! from the string
print(a.replace("Harry", "Mitali"))
print(a.split(" "))   # this will split the string into lists as soon it encouter a character like space for here.

blogHeading = "introduTiOn of Myself"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(str1.center(50))                    # this will center the string in the space
print(a.count("Debjeet"))

print(str1.endswith("!!!"))                 # returns true if the string is ending with the given word or substring

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))            # returns true if the string starts with the given word

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))      # this will return -1 as not found the substring
# print(str1.index("ishh"))     this will return error if not found

str1 = "Welcome To The 21st Console"
print(str1.isalnum())         #returns false as it is not number
str1 = "Welcome"
print(str1.isalpha())          # this will return truew as it is only character

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())   # returns all the printable characters and omit all the unprintable ones


# this isspace returns true when there is only white space in the string using tab or spacebar

str1 = "         "        #using Spacebar
print(str1.isspace())
str2 = "  "               #using Tab
print(str2.isspace())


str1 = "World Health Organization" 
print(str1.istitle())               # checks if the string is a title or not. ( here it will return true)

str2 = "To kill a Mocking bird"
print(str2.istitle())   

print(str1.title())                 # here it change the string into title.

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

