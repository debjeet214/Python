#  READING a file 

# way 1 to open a file (here you have to add the close() function at end to execute)

f  = open("ff.txt", "rt")   # we can access the file using the file name
te = f.read()
print(te)
f.close()

# Way 2 to open file (using 'with' keyword)

with open('ff.txt', 'a') as f:
    f.write("Hello guys")


# WRITE IN A FILE from start by replacing previous text

f = open("C:\\Users\\Debjeet Ghosh\\OneDrive\\Desktop\\file handling\\ff.txt", "w") # we can use the path of the file to accesss it too
f.write("Hello World.")
f.close()


# Write In A File at the end (APPENDING more text to a existing file)

f = open('C:\\Users\\Debjeet Ghosh\\OneDrive\\Desktop\\file handling\\ff.txt', 'a')
f.write("Hi there, is it working?")
f.close()

print(f)
