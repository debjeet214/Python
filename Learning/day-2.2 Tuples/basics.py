tup = (1, 23, 544, 21, True, 'Green', "cool baby")
print(type(tup), tup) 

print(len(tup))       # length of the tuple
tuples = (2)
print(type(tuples))   # this wil return as integer data as it is a single value
tuples =(2, )
print(type(tuples))   # using a comman will remove confusion and make it a tuple

# access the values using tuple

print(tup[0])
print(tup[-1])
print(tup[3])

# finding a value in the tuple

if 21 in tup:
  print("it is there in the tuple")

# slicing the tuple

tup2 = tup[1:5]
print(tup2)
