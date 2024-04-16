# explaining the sting methods

myname = 'my name is DEbjeeT GhosH. you know me?'
print("Actual line is = " + myname)

print("1. Upper Function" + myname.upper())    # make a copy of the actual string and change the case of the letters into uppercase

print("2. lower functions")
print(myname.lower())    # make a copy of the actual string and change the case of the letters into lowercase
print(myname.casefold())

print(myname.swapcase())    # this w3ill swap all the cases to other means, lower to upper an dupper to lower
print(myname.title())    # this will convert the string into a title like form


print(myname)            #no matter what method is applied, still the actual string stays as the same. as only copies are made and used to update
