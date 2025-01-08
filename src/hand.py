class Hand:
    def __init__(self):
        self.cards = []
        self.valid = True

    def add(self, card):
        if self.valid == True:
            self.cards.append(card)
    
            