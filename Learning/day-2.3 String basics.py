name =  'harry'
print("hello " + name)
print(name[3])

# using ofr loop printing all the characters in the string 

for character in name:
  print(character)

# string slicing 

fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4]) # including 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5])      # automatically add 0 at the start
print(fruit[0:-3])    # negative indexing 
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])
