import random
from .card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.__initialise_standard_deck()

    #initialises a standard deck of 52 cards
    def __initialise_standard_deck(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    #shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)
