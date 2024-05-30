''' The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality.

The *os* and *os.path* modules include many functions to interact with the file system.'''

import os
cwd = os.getcwd() # To get the location of the current working directory os.getcwd() is used.
print("Current working directory:", cwd)  # o/p = Current working directory: C:\Users\Debjeet Ghosh\OneDrive\Desktop\lolo
-
-
-
#  By using os.mkdir() method in Python is used to create a directory named path with the specified numeric mode. This method raises FileExistsError if the directory to be created already exists.

if(not os.path.exists("Data")):     # this path.exists checks if the directory is there or not.
    os.mkdir("Data")

for i in range(1, 101):
    os.mkdir(f"Data/Day {i}")

# we can rename the file names at the same time in python

for i in range(1, 101):
    os.rename(f"Data/Day {i}", f"Data/Tutorial {i}")
            # (source path)     (new name and source path)


# There is os.listdir() method in Python is used to get the list of all files and directories in the specified directory. If we don’t specify any directory, then the list of files and directories in the current working directory will be returned.

listing = os.listdir("Data")

for list in listing:
    print(list)

# to know what is inside a directory we can use this:
listing = os.listdir("Data")

for list in listing:
    print(os.listdir(f"data/{list}"))

# In os.path.getsize() function, python will give us the size of the file in bytes. To use this method we need to pass the name of the file as a parameter.

size = os.path.getsize("Data")
print("Size of the file is", size," bytes.")


# Different ways to delete a file in a directory.

os.rmdir("Data") # This will delete the file named "Data" only if the file is empty.
os.remove("Data")  # this will directly delete the file named "Data".


# This function gives the name of the operating system dependent module imported. The following names have currently been registered: ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’.


print (os.name)
# o/p = 1, 2..... try it out import os (posix)

