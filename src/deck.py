import random
from .card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.initialise_standard_deck()
        self.shuffle()

    def initialise_standard_deck(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)
