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
    guess = input("Enter your number here:").strip()
    count_of_attempts += 1
    if guess == "bye" or guess == "exit":
        print("Successfully exited the program")
        break
    elif not guess.isdigit():
        print("Please enter a valid Number")
    elif int(guess) > current_random_number:
        print("Too high!")
    elif int(guess) < current_random_number:
        print("Too low!")
    elif int(guess) == current_random_number:
        print("Congratulations! You guessed the number!")
        print(f"It took {count_of_attempts} attempts to guess the number.")