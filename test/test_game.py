import unittest
from src.game import Game
from src.player import Player
from unittest.mock import patch
import io
import sys

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game(1) 
        sys.stdout = io.StringIO() #redirects stdout to a buffer instead of the console
            
    def tearDown(self): 
        sys.stdout = sys.__stdout__ #resets stdout to the console
    
    #tests the deal_opening_hand method (scenario 1) and passes a mock input of 1 if an Ace is dealt
    @patch('builtins.input', side_effect=["1"])
    def test_deal_opening_hand(self, mock_input):
        self.game.players.append(Player("Test Player"))
        self.game.deal_opening_hand()
        self.assertEqual(len(self.game.players[0].hand.cards), 2)  #checks if the player has received 2 cards
    
    #tests the set_up_players method and passes a mock input of "Test" for the player name
    @patch('builtins.input', side_effect=["Test"])
    def test_set_up_players(self, mock_input):
        self.game.set_up_players()
        self.assertEqual(len(self.game.players), 1) #checks if the player has been added to the game




    