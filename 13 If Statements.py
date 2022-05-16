is_male = False

if is_male:
    print("You are a male")
else:
# "else" means otherwise.
    print("You are not a male")

# Here are more cases for if statement:
is_male = True
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

# You can also use "and" instead of "or"
is_male2 = True
is_tall2 = False
if is_male2 and is_tall2:
    print("You are a tall male")
else:
    print("You either not male or not tall or both")

# You can add more conditions with "elif" which stands for "else if"
is_male2 = False
is_tall2 = True
if is_male2 and is_tall2:
    print("You are a tall male")
elif is_male2 and not(is_tall2):
    print("You are a short male")
elif not(is_male2) and is_tall2:
    print("You are not a male but are tall")
else:
    print("You either not male or not tall or both")

# Use "not(xyz)" to check if something is true or not. In this case it will tell us if a person is tall or not OR a male