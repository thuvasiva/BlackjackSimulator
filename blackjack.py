from src.game import Game

def play():
    number_of_players = None
    while number_of_players == None:
        try:
            number_of_players = int(input("How many players are taking part in the game? "))
        except ValueError:
            print("Invalid input, please enter a number.")
    game = Game(number_of_players)
    game.set_up_players()
    game.deal_opening_hand()
    game.play_to_completion()
    
if __name__ == '__main__':
    play()
