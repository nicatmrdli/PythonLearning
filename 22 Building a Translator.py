def translate(phrase):
    translation = ""
    # This is the final result that will be returned at the end

    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
# This says "I want to print out the translation of whatever the user enters in
