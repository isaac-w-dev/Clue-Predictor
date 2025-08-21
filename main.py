from player import Player
from me import Me

class Main():
    def __init__(self):
        
        self.me = Me()
        self.player = Player()

        self.initialize_game()
        players = self.get_players()
        self.mark_false(players[1:-1], ['poison', 'greenroom', 'ms_scarlet'])
        self.mark_possible(players[-1], ['poison', 'greenroom', 'ms_scarlet'])
        self.main_menu()

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
                players.append(self.me)
                for i in range(self.num_of_players - 1):
                    players.append(Player())
                self.players = players
                break

    def initialize_game(self):
        self.get_player_number()
        for player in self.players[1:]:
            player.set_variable_attributes()
    
    def get_players(self):
        
        while True:
            try:
                print("Which players are involved?\n")
                for i, player in enumerate(self.players):
                    print(i, player.name)
                
                players = input().split()
                int_players = []
                returned_players = []
                valid_response = 0
                for player in players:
                    try:
                        int_players.append(int(player))
                    except:
                        print("Invalid response, restarting prompt...")
                        valid_response = 1
                if valid_response != 0:
                    raise Exception('One or more elements is invalid')
                
                if len(players) > len(self.players):
                    raise Exception('More entries than players')
            except:
                continue
            for num in int_players:
                returned_players.append(self.players[num])
            return returned_players

    def mark_false(self, player_list, clue_set):
        for player in player_list:
            for clue in clue_set:
                self.player.change_nested_data(player.possibilities, clue, False)
            print(player.name)
            print(player.possibilities)

    def mark_positive(self, player, clue_set, value):
        for clue in clue_set:
            self.player.change_nested_data(player.possibilities, clue, value)

    def main_menu(self):
        options = ['Question Player', 'Witness Question', 'Adjust Card']
        for i, option in enumerate(options):
            print(f'{i}     {option}')
        
        # for i , player in enumerate(self.players):
        #     print(i, player.name)

    # def question(self, questioner, questioned):
    #     for i , player in enumerate(self.players):
    #         print(i, player.name)
        


program = Main()
