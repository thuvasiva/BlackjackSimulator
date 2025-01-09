from .deck import Deck
class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.shuffle_deck()
    
    #returns the top card from the deck
    def deal(self):
        card = self.deck.cards.pop()
        return card
    
    #shuffles the deck
    def shuffle_deck(self):
        self.deck.shuffle()


    