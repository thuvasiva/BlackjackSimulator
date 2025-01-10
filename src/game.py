from .dealer import Dealer
from .player import Player
from .aiplayer import AIPlayer
from time import sleep

class Game:
    def __init__(self, no_of_players, activate_ai_player):
        self.dealer = Dealer()
        self.no_of_players = no_of_players
        self.players = []
        self.no_of_finished_players = 0
        self.activate_ai_player = activate_ai_player

    #creates the players for the game
    def set_up_players(self):
        print("|______Player Setup______|\n")
        if self.no_of_players < 1:
            print("You need at least 1 non-AI player to play the game.")
            print("Setting up a single-player game.\n")
            self.no_of_players = 1
        elif self.no_of_players > 4:
            print("You can have a maximum of 4 non-AI players in the game.")
            print("Setting up a 4 player game.\n")
            self.no_of_players = 4
        
        for i in range(self.no_of_players):
            user_input = input("Player " + str(i+1) + ": What is your name? ")
            print("Hello: " + user_input + "\n")
            new_player = Player(user_input)
            self.players.append(new_player)
        
        if self.activate_ai_player:
            self.players.append(AIPlayer("AI-Player"))
            self.no_of_players += 1

        print("Player set up complete!  \n")
        print("---------------------------------------")
    
    #deals an opening hand to each player and displays it
    def deal_opening_hand(self):
        print("|______Dealing Opening Hand______|\n")
        for player in self.players:
            print("Dealing opening hand for : " + player.name + "\n")
            player.hit(self.dealer)
            print(player.name + "'s hand " + str(player.hand.cards) + "\n")
            sleep(1) #sleeps for delay effect
            player.hit(self.dealer)
            print(player.name + "'s hand " + str(player.hand.cards) + "\n")
            if player.is_finished:
                print("Congratulations " + player.name + " your opening hand is a winning hand!")
                print("Your score is " + str(player.score))
                print("You will be declared as a winner at the end of the game.\n")
                self.no_of_finished_players += 1
            print("\n")
        print("---------------------------------------")
    
    #plays the game to completion
    def play_to_completion(self):
        print("|______Game Play______|\n")
        while self.no_of_finished_players < self.no_of_players:
            for player in self.players:
                if not player.is_finished:
                    print("Player " + player.name + " your cards are: " + str(player.hand.cards) + "\n")
                    print("Your current score is: " + str(player.score) + "\n")
                    player.make_hit_or_stand_decision(self.dealer)
                    print("\nYour cards following your decision are: " + str(player.hand.cards) + "\n")
                    print("Your new score is: " + str(player.score) + "\n")
                    if player.is_bust:
                        print(player.name + " went bust. \n")
                        self.no_of_finished_players += 1
                    elif player.is_finished:
                        print(player.name + " has finished. \n")
                        self.no_of_finished_players += 1
                    print("-------------------")
        self.determine_winner()

    #determines the winner(s) of the game
    def determine_winner(self):
        print("|______Game Over______|\n")
        remaining_players = []
        for player in self.players:
            if not player.is_bust:
                remaining_players.append(player)

        remaining_players.sort(key=lambda x: x.score, reverse=True)   
        try:
            maximum_score = remaining_players[0].score
        except IndexError:
            print("Unfortunately all player(s) went bust! :(")
        
        winners = []
        for player in remaining_players:
            if player.score == maximum_score:
                winners.append(player)

        #designates every player which hit the maximum valid score as a winner
        for player in winners:
            print(player.name + " - Congratulations! You won! Your score was: " + str(player.score))
                


        

            
    



    