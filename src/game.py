from .dealer import Dealer
from .player import Player
class Game:
    def __init__(self, no_of_players):
        self.dealer = Dealer()
        self.no_of_players = no_of_players
        self.players = []
        self.no_of_finished_players = 0

    def set_up_players(self):
        if self.no_of_players < 1:
            print("You need at least one player to play the game.")
            print("Setting up a single player game.")
            self.no_of_players = 1
        elif self.no_of_players > 4:
            print("You can have a maximum of 4 players in the game.")
            print("Setting up a 4 player game.")
            self.no_of_players = 4
        
        for i in range(self.no_of_players):
            user_input = input("Player " + str(i+1) + ": What is your name? ")
            print("Hello: " + user_input + "\n")
            new_player = Player(user_input)
            self.players.append(new_player)
        print("Player set up complete!  \n")
        print("-------------------------")
        
    def deal_opening_hand(self):
        for player in self.players:
            print("Dealing opening hand for : " + player.name + "\n")
            player.hit(self.dealer)
            player.hit(self.dealer)
            print(player.name + "'s hand " + str(player.hand.cards) + "\n")
            if player.is_finished:
                print("Congratulations your opening hand is a winning hand!")
                self.no_of_finished_players += 1
        print("-------------------------")
        
    def play_to_completion(self):
        while self.no_of_finished_players < self.no_of_players:
            for player in self.players:
                if not player.is_finished:
                    print("Player " + player.name + " your cards are: " + str(player.hand.cards) + "\n")
                    print("Your current score is: " + str(player.score) + "\n")
                    player.make_decision(self.dealer)
                    print("\nYour cards following your decision are: " + str(player.hand.cards) + "\n")
                    print("Your new score: " + str(player.score) + "\n")
                    if player.is_bust:
                        print(player.name + " went bust. \n")
                        self.no_of_finished_players += 1
                    elif player.is_finished:
                        print(player.name + " has finished. \n")
                        self.no_of_finished_players += 1
                    print("-------------------------")
        self.determine_winner()

    def determine_winner(self):
        remaining_players = []
        for player in self.players:
            if not player.is_bust:
                remaining_players.append(player)

        remaining_players.sort(key=lambda x: x.score, reverse=True)   
        try:
            maximum_score = remaining_players[0].score
        except IndexError:
            print("Everyone went bust!")
        
        winners = []
        for player in remaining_players:
            if player.score == maximum_score:
                winners.append(player)

        for player in winners:
            print(player.name + " - Congratulations! You won!")
                


        

            
    



    