num1 = float(input("Enter first number: "))
# NOTE: make sure to write "float" to convert the input to a number or a float.
operator = input("Enter first number: ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("invalid operator")