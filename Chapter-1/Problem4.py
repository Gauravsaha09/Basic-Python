# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that


import os

# get the current directory contents
path = "/"   # current directory
contents = os.listdir(path)

print("Contents of directory:", path)
for item in contents:
    print(item)
