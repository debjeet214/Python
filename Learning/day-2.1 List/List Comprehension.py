# list comprehension = list comprehension is a way to create a new list from an existing list in a single line of code
comp = [i for i in range(4)] 
print(comp)


#  create a new list of 1 to 10 all num's square
new_list = [i*i for i in range(1,11)]
print(new_list)

# create the list that contains only even values from 1 to 20
even_list = [i for i in range(1,21) if i%2 == 0]
print(even_list)
