from .deck import Deck
class Dealer:
    def __init__(self):
        self.deck = Deck()
    
    def deal(self):
        card = self.deck.cards.pop()
        return card
    
    def shuffle_deck(self):
        self.deck.shuffle()
        
    def reset_deck(self):
        self.deck.initialise_standard_deck()

    