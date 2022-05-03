is_male = True
is_tall = True

if is_male and is_tall:
    print("you are a male or tall or both")
elif is_male and not (is_tall):
    print("you are a short male")
elif not is_male and (is_tall):
    print("you are not a male but are tall")
else:
    print("you are not a male and not tall")

# you can also use "or" instead of "and"