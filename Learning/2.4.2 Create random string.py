# String.ascii_letters	    (It returns a random string that contains both uppercase and lowercase characters.
# String_ascii_uppercase	  (It is a random string method that only returns a string in uppercase characters.
# String.ascii_lowercase	  (It is a random string method that returns a string only in lowercase characters.
# String.digits	            (It is a random string method that returns a string with numeric characters.
# String.punctuation	      (It is a random string method that returns a string with punctuation characters.


import string
import random
# initializing size of string
N = 7
 
# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
 
# print result
print("The generated random string : " + str(res))
