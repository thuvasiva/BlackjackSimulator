import unittest
from src.deck import Deck
from src.card import Card

class DeckTestCase(unittest.TestCase):

    def setUp(self):  
        self.deck = Deck()

    def tearDown(self):  
        pass
    
    #tests there are 52 cards in deck
    def test_number_of_cards(self):  
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

        for card in self.deck.cards:
            self.assertIsInstance(card, Card)
    
    #tests there are 4 cards of each value in the deck
    def test_four_of_each_value(self):
        value_count = {'A':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10':0, 'J':0, 'Q':0, 'K':0}
        for card in self.deck.cards:
            value_count[card.value] += 1
        self.assertDictEqual(value_count, {'A':4, '2':4, '3':4, '4':4, '5':4, '6':4, '7':4, '8':4, '9':4, '10':4, 'J':4, 'Q':4, 'K':4})
    
if __name__ == '__main__':
    unittest.main()
