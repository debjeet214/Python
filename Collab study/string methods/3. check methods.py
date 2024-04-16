isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case

### some common example

stringing = 'The king of the ALberta is JACK 2 ? is not it'
print(stringing.isalnum())   # o/p is false as not all the characters in the string is number
print(stringing.isalpha())   # checks if all the characters are alphabetrs or not
print(stringing.isascii())   # checks if all the strings are ascii values
print(stringing.islower())   # checks if all the string characters are in lower case or not

string_val = " HI THERE ARE YOU OK "
print(string_val.isupper())  # checks if all the string characters are in upper case


