from src.game import Game

def play():
    number_of_players = None
    while number_of_players == None:
        try:
            number_of_players = int(input("How many players are taking part in the game? (1-4) "))
        except ValueError:
            print("Invalid input, please enter a number.")
    
    bot = None
    while (bot != "yes" and bot != "no"):
        bot = input("Would you like to compete with a bot (computer-controlled player) added to the game? 'yes' or 'no' ")
    
    if bot == "yes":
        bot = True
    elif bot == "no":
        bot = False

    game = Game(number_of_players, bot)
    game.set_up_players()
    game.deal_opening_hand()
    game.play_to_completion()
    
if __name__ == '__main__':
    play()
