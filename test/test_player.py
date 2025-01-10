import unittest
from src.player import Player
from src.card import Card
from unittest.mock import patch
from unittest.mock import Mock
import sys
import io

class PlayerTestCase(unittest.TestCase):

    def setUp(self):  
        self.player = Player("Test Player") 
        self.mock_dealer = Mock() #creates a mock dealer object
        sys.stdout = io.StringIO() #redirects stdout to a buffer instead of the console
        
    def tearDown(self):  
        sys.stdout = sys.__stdout__ #resets stdout to the console

    #tests the hit method of the player class (scenario 2)
    def test_hit(self):
        #sets up valid player hand and card to be dealt
        self.card1 = Card("Hearts", "4")
        self.card2 = Card("Clubs", "3")
        self.player.hand.add(self.card1) 
        self.player.update_score(self.card1)
        self.player.hand.add(self.card2)
        self.player.update_score(self.card2)
        self.mock_dealer.deal.return_value = Card("Diamonds", "10") #mocks the dealer's deal method to return 10 of Diamonds

        self.player.hit(self.mock_dealer) #calls hit

        self.assertEqual(len(self.player.hand.cards), 3) #tests if the player has received a card
        self.assertEqual(self.player.score, 17) #tests if the score has been updated correctly
    
    #tests the stand method of the player class (scenario 3)
    def test_stand(self):
        #sets up valid player hand
        self.card1 = Card("Diamonds", "7")
        self.card2 = Card("Clubs", "5")
        self.player.hand.add(self.card1) 
        self.player.update_score(self.card1)
        self.player.hand.add(self.card2)
        self.player.update_score(self.card2)

        self.player.stand() #calls stand

        self.assertEqual(len(self.player.hand.cards), 2) #tests if the player has not received any more cards
        self.assertEqual(self.player.is_finished, True) #tests if player has been designated as finished
        self.assertEqual(self.player.score, 12) #tests if the score is evaluated correctly

    #tests whether the player's hand is designated valid when the score is updated to less than 21 (scenario 4)
    def test_valid_when_hand_score_less_than_21(self):
        self.card1 = Card("Hearts", "2")
        self.card2 = Card("Clubs", "2")
        self.player.hand.add(self.card1) 
        self.player.update_score(self.card1)
        self.player.hand.add(self.card2)
        self.player.update_score(self.card2)
        self.mock_dealer.deal.return_value = Card("Clubs", "3")
        self.player.hit(self.mock_dealer) #hit updates score to 7

        self.assertEqual(self.player.hand.valid, True) #tests if the hand is designated valid
        self.assertEqual(self.player.score, 7) #asserts the score is 7 (2+2+3)

    #another test for scenario 4, tests boundary
    #tests whether the player's hand is designated valid when score is updated to 21 (scenario 4)
    def test_valid_when_hand_score_21(self):
        self.card1 = Card("Hearts", "4")
        self.card2 = Card("Clubs", "9")
        self.player.hand.add(self.card1) 
        self.player.update_score(self.card1)
        self.player.hand.add(self.card2)
        self.player.update_score(self.card2)
        self.mock_dealer.deal.return_value = Card("Hearts", "8")
        self.player.hit(self.mock_dealer) #hit updates score to 21

        self.assertEqual(self.player.hand.valid, True) #tests if the hand is designated valid
        self.assertEqual(self.player.score, 21) #asserts the score is 21

    #tests whether the player's hand is designated invalid when the score is updated to more than 21 (scenario 5)
    def test_invalid_when_hand_score_more_than_21(self):
        self.card1 = Card("Hearts", "8")
        self.card2 = Card("Clubs", "J")
        self.player.hand.add(self.card1)
        self.player.update_score(self.card1)
        self.player.hand.add(self.card2)
        self.player.update_score(self.card2)
        self.mock_dealer.deal.return_value = Card("Hearts", "6")
        self.player.hit(self.mock_dealer)

        self.assertEqual(self.player.is_bust, True) #tests if the player is designated as bust
        self.assertEqual(self.player.hand.valid, False) #tests if the hand is designated invalid
        self.assertEqual(self.player.score, 24) #asserts the score is 24 (8+10+6)

    #another test for scenario 5 (boundary)
    #tests whether the player's hand is designated invalid when the score is updated to 22 (scenario 5)
    def test_invalid_when_hand_score_22(self):
        self.card1 = Card("Hearts", "8")
        self.card2 = Card("Clubs", "J")
        self.player.hand.add(self.card1)
        self.player.update_score(self.card1)
        self.player.hand.add(self.card2)
        self.player.update_score(self.card2)
        self.mock_dealer.deal.return_value = Card("Clubs", "4")
        self.player.hit(self.mock_dealer) #hit updates score to 22
        
        self.assertEqual(self.player.is_bust, True) #tests if the player is designated as bust
        self.assertEqual(self.player.hand.valid, False) #tests if the hand is designated invalid
        self.assertEqual(self.player.score, 22) #asserts the score is 22 (8+10+4)
    
    #tests the score is evaluated to 21 when the hand contains a King and an Ace (scenario 6)
    @patch('builtins.input', side_effect=["1"]) #even when the user chooses the Ace worth to be 1
    def test_update_score_with_king_and_ace(self, mock_input):
        self.card1 = Card("Hearts", "K")
        self.card2 = Card("Clubs", "A")
        self.player.hand.add(self.card1)
        self.player.update_score(self.card1)
        self.player.hand.add(self.card2)
        self.player.update_score(self.card2)
        
        self.assertEqual(self.player.score, 21) #asserts the score is 21

    #tests the score is evaluated to 21 when the hand contains a King, a Queen and an Ace (scenario 7)
    @patch('builtins.input', side_effect=["1"])
    def test_update_score_with_king_queen_and_ace(self, mock_input):
        self.card1 = Card("Hearts", "K")
        self.card2 = Card("Clubs", "Q")
        self.card3 = Card("Hearts", "A")
        self.player.hand.add(self.card1)
        self.player.update_score(self.card1)
        self.player.hand.add(self.card2)
        self.player.update_score(self.card2)
        self.player.hand.add(self.card3)
        self.player.update_score(self.card3)
        
        self.assertEqual(self.player.score, 21) #asserts the score is 21
    
    #tests the score is evaluated to 21 when the hand contains a Nine, an Ace and an Ace (scenario 8)
    @patch('builtins.input', side_effect=["11", "11"]) #user chooses both aces to be worth 11
    def test_update_score_with_nine_ace_and_ace(self, mock_input):
        self.card1 = Card("Hearts", "9")
        self.card2 = Card("Clubs", "A")
        self.card3 = Card("Hearts", "A")
        self.player.hand.add(self.card1)
        self.player.update_score(self.card1)
        self.player.hand.add(self.card2)
        self.player.update_score(self.card2)
        self.player.hand.add(self.card3)
        self.player.update_score(self.card3)
        
        self.assertEqual(self.player.score, 21) #asserts the score is 21
    
if __name__ == '__main__':
    unittest.main()