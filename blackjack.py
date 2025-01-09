from src.game import Game

def play():
    number_of_players = None
    while number_of_players == None:
        try:
            number_of_players = int(input("How many players are taking part in the game? (1-4) "))
        except ValueError:
            print("Invalid input, please enter a number.")
    
    ai_player = None
    while (ai_player != "yes" and ai_player != "no"):
        ai_player = input("Would you like to play with an additional AI (computer-controlled) player? 'yes' or 'no' ")
    
    if ai_player == "yes":
        ai_player = True
    elif ai_player == "no":
        ai_player = False

    game = Game(number_of_players, ai_player)
    game.set_up_players()
    game.deal_opening_hand()
    game.play_to_completion()
    
if __name__ == '__main__':
    play()
