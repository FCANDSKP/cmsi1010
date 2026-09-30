# Generate a random number between 1 and 1000.
#
# Ask the user to guess the number. In your prompt, let the user know they
# can type 'bye' or 'exit' to quit the program.
#
# If their guess is not made up entirely of digits, print "Please enter a valid
# number" and ask them to guess again.
#
# If the guess is too high, print "Too high!" and continue asking.
#
# If the guess is too low, print "Too low!" and continue asking.
#
# If the guess is correct, print "Congratulations! You guessed the number!" along
# with the number of attempts it took to guess the number. Start over with a new
# random number. Make sure to zero out the number of attempts.
#
# Please note: There are likely to be a number of Python guessing games online,
# and most GenAI systems can probably write this for you. Don’t rely on them,
# as they rob you of a chance to practice your Python skills and they might not
# even be correct. Perhaps, worse, they might not follow the instructions
# exactly as given.
# ----------------------------------------------------------------------

import random
random_number = range(1, 1001)
current_random_number = random.choice(random_number) 

count_of_attempts = 0

print("Welcome to the Number Guesser!")
print("Guess a number between 1 and 1000.")
print("Type 'bye' or 'exit' to quit the program")
print()
keep_going = True
while True:
    guess = int(input("Enter your number here:").strip())
    count_of_attempts += 1
    if guess > current_random_number:
        print("Too high!")
    elif guess < current_random_number:
        print("Too low!")
    elif guess == current_random_number:
        print("Congratulations! You guessed the number!")
        print(count_of_attempts)
    elif guess == "bye" or guess == "exit":
        print("Successfully exited the program")
        break
    else:
        print("Please enter a valid Number")