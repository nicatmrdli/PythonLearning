# The try block lets you test a block of code for errors.
try:
    number = int(input("Enter a number: "))
    print(number)
 except:
    print("Invalid Input")
# The except block lets you handle the error. However using one except block is usually too broad.


# You can use multiple except blocks to make it more efficient.
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")
# You can write the error name next to the except block to specify the type of error that you want to catch.


# You can print out a specific error as well.
try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
# If you add "as" next to the error name and then name it (in this case err), it will print the error name instead.