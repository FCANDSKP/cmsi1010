from dataclasses import dataclass
from random import shuffle


@dataclass(frozen=True)
class Card:
    suit: str
    rank: int

    def __post_init__(self):
        if self.suit not in ("S", "H", "D", "C"):
            raise ValueError("suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")

    def __str__(self):
        suit_str = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}[self.suit]
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(
            self.rank, str(self.rank))
        return f"{rank_str}{suit_str}"


def standard_deck():
    return [Card(suit, rank) for suit in "SHDC" for rank in range(1, 14)]


def shuffled_deck():
    cards = standard_deck()
    shuffle(cards)
    return cards


def deal_one_five_card_hand():
    deck = shuffled_deck()
    return set(deck[:5])


def deal(number_of_hands, cards_per_hand):
    if not isinstance(number_of_hands, int):
        raise TypeError("Hands must be an integer")
    if not isinstance(cards_per_hand, int):
        raise TypeError("Cards per hand must be an integer")
    if number_of_hands < 1 or cards_per_hand < 1:
        raise ValueError("Needs to at least be one")
    if number_of_hands * cards_per_hand > 52:
        raise ValueError("I don't have that many cards")
    all_hands = []
    deck = shuffled_deck()
    for i in range(number_of_hands):
        hand = set(deck[i*cards_per_hand: (i+1)*cards_per_hand])
        all_hands.append(hand)
    return all_hands



def poker_classification(hand):
    if not isinstance(hand, set):
        raise TypeError('Hand must be a set for poker')
    if len(hand) != 5:
        raise ValueError('Must have exactly 5 cards')

    ranks = sorted(card.rank for card in hand)
    counts = sorted((ranks.count(rank) for rank in set(ranks)), reverse=True)
    flush = len({card.suit for card in hand}) == 1
    straight = (ranks == [1, 10, 11, 12, 13]
                or len(set(ranks)) == 5 and ranks[-1] - ranks[0] == 4)

    categories = [
        (straight and flush and set(ranks) == {1, 10, 11, 12, 13}, "Royal Flush"),
        (straight and flush, "Straight Flush"),
        (counts == [4, 1], "Four of a Kind"),
        (counts == [3, 2], "Full House"),
        (flush, "Flush"),
        (straight, "Straight"),
        (counts == [3, 1, 1], "Three of a Kind"),
        (counts == [2, 2, 1], "Two Pair"),
        (counts == [2, 1, 1, 1], "One Pair"),
    ]
    return next((name for matches, name in categories if matches), "High Card")

