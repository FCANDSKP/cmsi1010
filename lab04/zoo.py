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