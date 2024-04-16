# explaining the sting methods

myname = 'my name is DEbjeeT GhosH. you know me?'
print("Actual line is = " + myname)

print("1. Upper Function" + myname.upper())    # make a copy of the actual string and change the case of the letters into uppercase

print("2. lower functions")
print(myname.lower())    # make a copy of the actual string and change the case of the letters into lowercase
print(myname.casefold())

print(myname.swapcase())    # this w3ill swap all the cases to other means, lower to upper an dupper to lower
print(myname.title())    # this will convert the string into a title like form

find_char = myname.find('is')
print( "3. Find a specific word index = " + str(find_char))   # this will return the index position of the particular  letter in the string if it exists, otherwise returns null

print("4. Make the first character capital = " + myname.capitalize()) # this will make the first charater upper case.

print(myname.split('is', 5))   # split the string at the first occurrence of

print(myname.count('me'))  # count the no of times a value occur in the string
print(myname)            # still the actual string stays as the same.
