import unittest
from src.deck import Deck


class DeckTestCase(unittest.TestCase):

    def setUp(self):  
        self.deck = Deck()

    def tearDown(self):  
        pass
    
    #tests there are 52 cards in deck
    def test_number_of_cards(self):  
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)
    
    #tests there are 4 aces in deck
    def test_number_of_aces(self):
        number_of_aces = 0
        for card in self.deck.cards:
            if card.value == "A":
                number_of_aces += 1
        self.assertEqual(number_of_aces, 4)

    #tests there are 4 kings in deck
    def test_number_of_kings(self):
        number_of_kings = 0
        for card in self.deck.cards:
            if card.value == "K":
                number_of_kings += 1
        self.assertEqual(number_of_kings, 4)
    
    #tests there are 4 twos in deck
    def test_number_of_twos(self):
        number_of_twos = 0
        for card in self.deck.cards:
            if card.value == "2":
                number_of_twos += 1
        self.assertEqual(number_of_twos, 4)

    
if __name__ == '__main__':
    unittest.main()
