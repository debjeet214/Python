'''Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.'''


# Declearing a dictionary
dic1 = {
    "Name": "Debjeet",
    "Roll": "273221",
    "age": "19"
}

print(dic1["Name"])
print(f"The Roll of {dic1['Name']} is {dic1['Roll']}.")


# Printing the keys and values from the dictionary.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) 
print(info.keys())          # seperately only print the keys
print(info.values())        # only prints the values of the present keys

# using the loop we can print all too 
for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")
  

print(info['error_check'])   # if the used key is not in the dictionary then, it will return error
print(info.get('eligibles'))   # but using get function won't return error.
