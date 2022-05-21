secret_word = "neezy"
guess = ""
guess_count = 0
# This shows how many times a user input his guess, since there are no inputs yet, you should write 0.
guess_limit = 3
# This shows the max limit of how many times a user has a chance to guess.
out_of_guesses = False
# This shows that a user still has guesses left.

while guess != secret_word and not(out_of_guesses):
    # Meaning that if a word isn't equals to a secret word and if the user isn't out of guess, then it wont stop looping
    if guess_count < guess_limit:
        # This shows that a guess count should be less than the guess limit
        guess = input("Enter Guess: ")
        # If a user still has guesses remaining then the user will still be able to enter input.
        guess_count += 1
        # This shows that the guess count should add up to 3 (the guess limit) each time a user enters a wrong word.
    else:
        out_of_guesses = True
        # This shows that a user ran out of guesses

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
    # This will be displayed if a user fails to find a correct word
else:
    print("You win!")
    # This will be displayed if a user finds the correct word