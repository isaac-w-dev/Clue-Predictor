from player import Player
from me import Me
from functions import Functions
from evidence import evidence

import copy

class Main():
    def __init__(self):
        self.clues = copy.deepcopy(evidence)
        self.me = Me()
        self.player = Player()
        self.functions = Functions()

        self.initialize_game()
        self.main_menu()

    def get_player_number(self):
        players = []
        while True:
            try:
                self.num_of_players = int(input('How many players are in the game including yourself?: '))
                if self.num_of_players < 2:
                    ## Change to 3 when testing finished
                    print("Can't have less than 3 players.")
                    raise Exception("Can't have less than 3 players.")
                elif self.num_of_players > 6: 
                    print("Can't have more than 6 players.")
                    raise Exception("Can't have more than 6 players.")
            except:
                print('Invalid entry. Restarting prompt.')
                continue
            else:
                print(f'The number of players is {self.num_of_players} is this correct? Y/N')
                if input().upper() != 'Y': continue
                players.append(self.me)
                for i in range(self.num_of_players - 1):
                    players.append(Player())
                self.players = players
                break


    def initialize_game(self):
        self.get_player_number()
        for player in self.players[1:]:
            player.set_variable_attributes(self.num_of_players)


    def get_players(self):
        while True:
            try:
                print("Which players are involved?\nStart with initiator first, then enter in the order asked")
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
                if valid_response != 0: raise Exception('One or more elements are invalid')
                
                if len(players) > len(self.players): raise Exception('More entries than players')
            except:
                continue
            for num in int_players:
                returned_players.append(self.players[num])
            return returned_players

    # def check_for_deductions(self):
    #     remove_from_set()
    #     update_possibilities()
    #     convert_values_true()
    #     compare_values_to_num_cards()
    #     update_general_card()


    def main_menu(self):
        options = ['Question', 'Adjust Card', 'Rush to the Finish']
        for i, option in enumerate(options):
            print(f'{i}     {option}')
        self.question(self.clues, self.players)
        # if entry == 0:
        #     self.question()
        # if entry == 1:
        #     self.adjust_card()
        # if entry == 2:
        #     self.rush_finish()


    # def check_order(self, order):
    #     if order[0] == 0:

    def question(self, dictionary, players):
        test = []
        for type, selection in dictionary.items():
            print(f"Select the number corresponding to the {type} provided.")
            i = 0
            selection_array = selection.keys()
            for i, key in enumerate(selection_array):
                print(f"{i}     {key}")
                i += 1
            order = self.functions.get_int(-1, len(selection.keys()), 1)
            selection_list = list(selection_array)
            for item in order:
                test.append(selection_list[item])
            print("Order:", order)
            print("Selection Array:", selection_list)
            print("Test: ", test)
            if len(players) > 2:
                for player in players[1:-1]:
                    self.functions.change_nested_data(player.possibilities, test, False)
            else:
                players[-1].set_list.append(test)
                print(players[-1].set_list)
            # if players[0].name == 'Me':

program = Main()
