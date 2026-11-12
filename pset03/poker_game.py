# ----------------------------------------------------------------------
# This is the file poker_game.py
#
# Write a program that repeatedly prompts the user for a number of players 
# in a poker game, then, if the input is valid, deals each player a 5-card hand 
# then prints each hand and its poker classification.
#
# Allow an input of "bye" or "exit" (after stripping and lowercasing 
# the user's input) to quit the program.
#
# The program should not crash or raise an exception if the user enters
# something that is not a valid number of players, or if the user
# enters a number of players that is not between 2 and 10. Instead,
# the program should print an error message and prompt the user again
# for a valid number of players.
# 
# Remember that for this assignment, you will also be creating a module
# for cards in cards.py. Figure out the import statement to use in this file 
# to import the functions and classes you need from that module.
#
# Here is an example run:
#
# Enter the number of players(2-10): 10
# 9♦ 6♠ 5♥ 9♠ A♠ is a One Pair
# 6♦ 7♠ 5♦ Q♠ 2♠ is a High Card
# 2♥ 8♥ 4♥ 4♦ 3♣ is a One Pair
# K♥ 3♥ 10♠ J♦ 10♥ is a One Pair
# K♠ J♥ 4♣ 8♠ 7♦ is a High Card
# 6♣ 6♥ A♣ A♦ 3♦ is a Two Pair
# Q♣ A♥ J♠ K♦ 9♣ is a High Card
# 9♥ Q♦ 8♣ 7♣ 7♥ is a One Pair
# 5♣ 2♦ 10♦ K♣ 4♠ is a High Card
# 2♣ 8♦ J♣ 10♣ 5♠ is a High Card
#
# Enter the number of players(2-10): bye
# ----------------------------------------------------------------------

import random

from cards import Card, deal, poker_classification

while True:
    players = input("Enter the ammount of players here:").strip()
    if input == "bye" or input == "exit": 
        print("Successfully exited the Program")
        break
    if not isinstance(players, int):
        raise ValueError("Players must be an integer")
    if players < 2 or players > 10:
        raise ValueError("Can only be between 2 and 10 players")
    
    