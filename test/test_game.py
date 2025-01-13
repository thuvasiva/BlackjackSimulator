import unittest
from src.game import Game
from src.player import Player
from unittest.mock import patch
import io
import sys

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game(1, False) 
        sys.stdout = io.StringIO() #redirects stdout to a buffer instead of the console
            
    def tearDown(self): 
        sys.stdout = sys.__stdout__ #resets stdout to the console
    
    #tests the deal_opening_hand method (scenario 1) 
    @patch('builtins.input', side_effect=["1"]) #passes a mock input of 1 if an Ace is dealt
    def test_deal_opening_hand(self, mock_input):
        self.game.players.append(Player("Test Player"))

        self.game.deal_opening_hand()

        self.assertEqual(len(self.game.players[0].hand.cards), 2)  #checks if the player has received 2 cards
    
    #tests the set_up_players method 
    @patch('builtins.input', side_effect=["Test"]) #passes a mock input of "Test" for the player name
    def test_set_up_players(self, mock_input):
        self.game.set_up_players()

        self.assertEqual(len(self.game.players), 1) #checks if the player has been added to the game

    #tests the determine_winner method with a single winner
    def test_determine_winner_single_winner(self):
        #creates a player with a score of 21 and another with a score of 19
        player1 = Player("Test Player")
        player2 = Player("Test Player 2")
        player1.score = 21
        player2.score = 19
        self.game.players.append(player1)
        self.game.players.append(player2)
        self.game.no_of_players += 1
    
        self.game.determine_winner()

        self.assertEqual(len(self.game.winners), 1) #checks if there is only one winner
        self.assertIn(player1, self.game.winners) #checks if the correct player has been declared as the winner

    #tests the determine_winner method with multiple winners
    def test_determine_winner_multiple_winners(self):
        #creates two players with a score of 18 and another with a score of 14
        player1 = Player("Test Player")
        player2 = Player("Test Player 2")
        player3 = Player("Test Player 3")
        player1.score = 14
        player2.score = 18
        player3.score = 18
        self.game.players.append(player1)
        self.game.players.append(player2)
        self.game.players.append(player3)
        self.game.no_of_players += 2

        self.game.determine_winner()

        self.assertEqual(len(self.game.winners), 2) #checks if there are two winners
        self.assertIn(player2, self.game.winners)
        self.assertIn(player3, self.game.winners)

    #tests the determine_winner method with no winners
    def test_determine_winner_no_winner(self):
        #creates two bust players with a score of 22 and another with a score of 27
        player1 = Player("Test Player")
        player2 = Player("Test Player 2")
        player1.score = 22
        player1.is_bust = True
        player2.score = 27
        player2.is_bust = True
        self.game.players.append(player1)
        self.game.players.append(player2)
        self.game.no_of_players += 1

        self.game.determine_winner()

        self.assertEqual(len(self.game.winners), 0) #checks if there are no winners
    


if __name__ == '__main__':
    unittest.main()



    