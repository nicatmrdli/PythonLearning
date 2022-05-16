def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))

# Here is the list of every "comparison operators":
# "==" for equal,
# "!=" for not equal,
# "<" greater,
# ">" less,
# ">=" greater or equal,
# "<=" less or equal