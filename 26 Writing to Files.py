# This is how you append a file
employee_file = open("25 Reading files txt", "a")

employee_file.write("Toby - Human Resources")
# This code will add a new line to the file.
employee_file.close()


###
employee_file = open("25 Reading files txt", "a")

employee_file.write("\nKelly - Customer Service")
# You can use "\n" to add a new line.
# "\n" also indicates the end of the text and its called "escape character".

employee_file.close()


### This code will overwrite the whole document with the selected name in this case, "Kelly - Customer Service".
employee_file = open("25 Reading files txt", "w")

employee_file.write("\nKelly - Customer Service")

employee_file.close()


###
employee_file = open("25 Reading files txt1", "w")
# If you edit the location name a bit, python will create a new text file and write the employee name on that file.
employee_file.write("\nKelly - Customer Service")

employee_file.close()


### You can also create HTML document instead of a regular text file.
employee_file = open("index.html", "a")

employee_file.write("<p>This is HTML</p>")

employee_file.close()