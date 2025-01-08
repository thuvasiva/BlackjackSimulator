from .deck import Deck
class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.shuffle_deck()
    
    def deal(self):
        card = self.deck.cards.pop()
        return card
    
    def shuffle_deck(self):
        self.deck.shuffle()


    