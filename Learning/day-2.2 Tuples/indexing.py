# Tuple Indexes
# Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.

# I. Positive Indexing: As we have seen that tuple items have index, as such we can access items using these indexes.

country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]  

print(country[0])
print(country[1])
print(country[2])

#  II. Negative Indexing: Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])


# III. Check for item: We can check if a given item is present in the tuple. This is done using the in keyword.

country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")

#  IV. Range of Index:  Syntax: Tuple[start : end : jumpIndex]  (jump Index is optional. We will see this in given examples.)

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes where the range is properly given here


animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #range is not given therefore the compiler itself takme here the length of the tuple meaning it will print from 4 to index len-1 
print(animals[-4:])     


animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #in this case the it is take as animal[0:6],  do it will print values from 0 to 5 values



animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #this mans it will print all the second placed values in the tuples from index 0 to end
print(animals[-9:-1:2]) #equal to previous

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])
