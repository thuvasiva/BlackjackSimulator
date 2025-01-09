from src.player import Player
from time import sleep
import random

class AIPlayer(Player):
    def make_hit_or_stand_decision(self, dealer):
        sleep(1)
        if self.score < 17:
            print("AI-Player has chosen to hit.")
            self.hit(dealer)
        else:
            print("AI-Player has chosen to stand.")
            self.stand()
            
    def make_ace_value_decision(self):
        return random.choice([1,11])

    