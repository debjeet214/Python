#  couting using loop
x = 0
for thing in [90, 23, 12, 8, 98, 34, 1]:
    x = x+1
    print(x, thing)

print("The in total counting is:", x)


#  summing using loop
x = 0
count = 0
for thing in [90, 23, 12, 8, 98, 34, 1]:
    x = x + thing
    count = count +1
    print(count, x)

print("The sum of al values are:", x)


#  finding the average of all values
sum = 0
count = 0
for thing in [90, 23, 12, 8, 98, 34, 1]:
    sum = sum + thing
    count = count +1

print("The average of all values are", sum/count)


# searching in loop using a boolean value.
found = False
for thing in [90, 23, 12, 8, 98, 34, 1]:
    if thing == 8:
        found = True
        print(thing, found)
print("All done!")


# fidn the largest and smallest value in the list
largest = None
smallest = None
for thing in [90, 23, 12, 8, 98, 34, 1]:
    if largest is None or thing > largest:
        largest = thing
    if smallest is None or thing < smallest:
        smallest = thing
print("The Smallest number is:", smallest)
print("The largest number is ", largest)
