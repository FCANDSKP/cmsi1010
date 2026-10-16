templates = [
    {
        "text": "A :adjective ghost is behind you!", 
        "author": "rtoal"
    },
    {
        "text": "Some :adjective :creature with a :weapon is eating :dessert", 
        "author": "rtoal"
    },
    {
        "text": "Look! There's a :adverb :adjective :verb a :noun in :place", 
        "author": "class"
    }, 
    {
        "text": "This years haunted house is at :location",
        "author": "kp"
    }, 
    {
        "text": "The monster :verb the :number :food",
        "author": "kp"
    }, 
    {
        "text": "We :verb to the :location, where we discovered a :object on the floor",
        "author": "kp"
    }, 
    {
        "text": "Theres :number :food for you to grab, but you can only have them if you can find the :object",
        "author": "kp"
    }, 
    {
        "text": "The little kid shouted something about a :adjective :verb :noun",
        "author": "kp"
    }, 
    {
        "text": ":person always told me to :verb with my friends",
        "author": "kp"
    }, 
    {
        "text": "Happy :noun day! Today is :month :date",
        "author": "kp"
    }, 
]

yes_answers = {"yes", "si", "oui" "yup", "bet", "yep", "Y"}

import random
import re

while True:
    current_template = random.choice(templates)
    text = current_template["text"]
    for word in re.findall(r":([A-Za-z]+)", text):
        while True:
            answer = input(f"Enter a {word} with 1-30 characters: ").strip()
            if 1 <= len(answer) <= 30: 
                break
            print("Error: Input not within limit")
        text = text.replace(f":{word}", answer, 1)

    print(text)
    print(f"\nAuthor: {current_template['author']}")

    play_again = input("\n\n\nWould you like to play again? ").strip().casefold()
    if play_again not in yes_answers:
        print("Thank you for playing!")
        break