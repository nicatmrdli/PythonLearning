# You can use "open" to read different file.
open("25 Reading files txt", "r")
# You first need to select the file name or location and then select the mode that you want to do.
# "r" = read, "w" = write or change the file, "a" = append new info to the file, "r+" = read and write the file.

employee_file = open("25 Reading files txt", "r")
# Before reading a file you have to store it in a variable.

employee_file.close()
# Make sure to close file with this code at the end.


###
employee_file = open("25 Reading files txt", "r")
print(employee_file.readable())
# This will tell if the file itself is readable or not
print(employee_file.read())
# This will read every info on the file
print(employee_file.readline())
# This will read the first line. if you duplicate it, it will read the second line as well, etc.
print(employee_file.readlines())
# This will read every line in a list. This is more efficient than ".readline" code.


# You can also use for loops.
employee_file = open("25 Reading files txt", "r")
for employee in employee_file.readlines():
    print(employee)

print(employee_file.readable())