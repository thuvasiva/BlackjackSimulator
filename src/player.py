from .hand import Hand
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.score = 0
        self.is_bust = False
        self.is_finished = False

    def hit(self, dealer):
        card = dealer.deal()
        self.hand.add(card)
        self.update_score(card)
        self.evaluate_status()
                
    def stand(self):
        optimized = self.optimize_score()
        if optimized > self.score and optimized <= 21:
            self.score = optimized
        self.is_finished = True

    def update_score(self, card):
        face_value = card.value
        if face_value == "A":
            value = self.make_ace_value_decision()
        elif face_value == "K" or face_value == "Q" or face_value == "J":
            value = 10
        else:
            value = int(face_value)

        unoptimized = self.score + value
        optimized = self.optimize_score()

        if (optimized == 21) or (unoptimized > 21 and optimized <= 21):
            self.score = optimized
        else:
            self.score = unoptimized
        
    def optimize_score(self):
        card_wise_score = []
        
        for card in self.hand.cards:
            if card.value == "K" or card.value == "Q" or card.value == "J":
                card_wise_score.append(10)
            elif card.value == "A":
                card_wise_score.append(1)
            else:
                card_wise_score.append(int(card.value))
        
        for i in range(len(card_wise_score)):
            if card_wise_score[i] == 1 and sum(card_wise_score) + 10 <= 21:
                card_wise_score[i] = 11
        
        optimized = sum(card_wise_score)
        return optimized
    
    def evaluate_status(self):
        if self.score > 21:
            self.hand.is_valid = False
            self.is_bust = True
            self.is_finished = True
        elif self.score == 21:
            self.is_finished = True
    
    def make_hit_or_stand_decision(self, dealer):
        decision = None
        while(decision != "hit" and decision != "stand"):
            decision = input("Do you want to 'hit' or 'stand'? ")
            if decision == "hit":
                self.hit(dealer)
            elif decision == "stand":
                self.stand()

    def make_ace_value_decision(self):
        value = None
        while(value != 1 and value != 11):
            try:
                value = int(input(self.name + ", you've been dealt an Ace! Would you like it to be worth 1 or 11? "))
            except ValueError:
                print("Invalid input, please enter either 1 or 11.")
        return value
        
         


    



        