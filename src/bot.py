from src.player import Player
from time import sleep
import random

class Bot(Player):
    #overrides the make_hit_or_stand_decision method to make a decision based on the score
    def make_hit_or_stand_decision(self, dealer):
        sleep(1) #sleeps for delay effect
        if self.score < 17:
            print("Bot has chosen to hit.")
            self.hit(dealer)
        else:
            print("Bot has chosen to stand.")
            self.stand()
    
    #overrides the make_ace_value_decision method to randomly choose between 1 and 11
    def make_ace_value_decision(self):
        return random.choice([1,11])

    