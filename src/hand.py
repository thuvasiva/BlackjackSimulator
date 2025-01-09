class Hand:
    def __init__(self):
        self.cards = []
        self.valid = True

    #adds a card to the hand if the hand is valid
    def add(self, card):
        if self.valid == True:
            self.cards.append(card)
    
            