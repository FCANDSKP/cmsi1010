from cards import Card, deal, poker_classification

while True:
    response = input("Enter the number of players (2-10): ").strip().lower()
    if response in ("bye", "exit"):
        print("Goodbye")
        break

    try:
        players = int(response)
    except ValueError:
        print("Your response must be an integer")
        continue

    if not 2 <= players <= 10:
        print("Please enter a number between 2 and 10")
        continue

    hands = deal(players, 5)
    for hand in hands:
        cards = " ".join(str(card) for card in hand)
        classification = poker_classification(hand)
        print(f"{cards} is a {classification}")
    
    