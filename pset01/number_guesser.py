# ----------------------------------------------------------------------
# This is the file number_guesser.py
#
# The intent is to give you practice writing a complete, interactive
# Python program.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#
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

def show_help():
    print("Type 'help' to see this list again")
    print("Type 'see' to see all the animals")
    print("Type 'pet' followed by the animal's name to pet that animal")
    print("Type 'bye' to leave the zoo and exit the program")

def show_all_animals():
    print("The animals in the zoo are:")
    print("1. Clover the Bunny 🐇")
    print("2. Coco the Baby Goat 🐐")
    print("3. Arno the Alligator 🐊")
    print("4. Dan the Duck 🦆")

def pet_animal(animal):
    if animal == ("Clover").strip().lower(): 
        print("Clover is so happy! ❤️")
    elif animal == ("Coco").strip().lower():
        print("Coco the Baby Goat thanks you! 🥰")
    elif animal == ("Arno").strip().lower(): 
        print("Actually, we cannot allow you to pet Arno. ⛔️")
    elif animal == ("Dan").strip().lower():
        print("Dan the Duck quacks happily! 😊")
    else:
        print("Sorry, I don't know that animal")

print("Welcome to the Petting Zoo!")
print("Type 'help' to get a list of all the things you can do")
print()
keep_going = True
while True:
    response = input("What would you like to do?").strip().lower()
    if response == "help":
        show_help()
    elif response == "see":
        show_all_animals()
    elif response.startswith("pet "):
        animal = response[4:].strip()
        pet_animal(animal)
    elif response == "bye":
        print("Goodbye!")
        break
    else:
        print("Sorry, I don't understand that command")