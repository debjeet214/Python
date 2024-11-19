# sort function: by default sort the collection

print(sorted([3, 88, -7, 56, 9, 21, -76, 55])) # sorting numbers

print(sorted(['santanu', 'ayesha', 'mitali', 'Debjeet'])) # Debjeet is at first as capital 'D' has a smaller ASCII value

# We can provide the key to the function for better functioning
print(sorted(['swatakshi', 'Rishi', 'mitali', 'Debjeet'], key = len)) # sort depending on the length of the word


# Sort by title by splitting and sorting using normal function
def func(names):
  return names.split()[1]

data = ['rajankita saha', 'Babita mandal', 'Mitali rath']
print(sorted(data, key = func))


# sort by title by splitting and sorting using lambda function
data = ['rajankita saha', 'Babita mandal', 'Mitali rath']
print(sorted(data, key = lambda names:names.split()[1]))
