from player import Player
from me import Me

class Main():
    def __init__(self):
        self.me = Me()
        self.initialize_game()

    def get_player_number(self):
        players = []
        while True:
            try:
                self.num_of_players = int(input('How many players are in the game including yourself?: '))
                if self.num_of_players < 2: 
                    print("Can't have less than 2 players.")
                    raise Exception("Can't have less than 2 players.")
                elif self.num_of_players > 10: 
                    print("Can't have more than 10 players.")
                    raise Exception("Can't have more than 10 players.")
            except:
                print('Invalid entry. Restarting prompt.')
                continue
            else:
                for i in range(self.num_of_players - 1):
                    players.append(Player())
                self.players = players
                break

    def initialize_game(self):
        self.get_player_number()
        for player in self.players:
            player.set_variable_attributes()

program = Main()
