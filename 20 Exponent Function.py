# Exponent Function allows you to raise a number to desired power using For Loops

def raise_to_power(base_num, pow_num):
    # This shows that the base number is going to be taken to a power number.
    result = 1
    # Result is going to store the actual result of doing the math.
    for index in range(pow_num):
        # This means that python is going to loop through range of numbers up to but not including the power number
        result = result * base_num
        # Every loop its going to multiply result by base number to first equal the base num to 1 and then remultiply it
    return result

print(raise_to_power(3, 4))