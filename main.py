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


                # self.num_of_players = int(input('How many players are in the game including yourself?: '))
                self.num_of_players = 4


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



                # print(f'The number of players is {self.num_of_players} is this correct? Y/N')
                # if input().upper() != 'Y': continue



                players.append(self.me)
                for i in range(self.num_of_players - 1):
                    players.append(Player())
                self.players = players
                break


    def initialize_game(self):


        names = ["Mom", "Dad", "Ben", "Addie", "Leah"]
        num_cards = 4
        player_sets = [['ms_scarlet', 'green_room', 'knife'],['ms_scarlet', 'conservatory', 'knife'], ['ms_scarlet', 'green_room', 'poison']]

        self.get_player_number()
        for i, player in enumerate(self.players[1:]):


            player.set_variable_attributes(names[i], num_cards)
            player.set_list.append(player_sets[i])


        for player in self.players[1:]:
            print("Name:", player.name, "\nNumber of Cards:", player.num_of_cards, "\n\n")


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
        self.functions.deductions_from_true(self.players[0].possibilities, self.players[1:])
            # player.filter_false()
        # while True:
        #     options = ['Question', 'Adjust Card', 'Rush to the Finish']
        #     for i, option in enumerate(options):
        #         print(f'{i}     {option}')
        #     self.question(self.clues)


    def question(self, dictionary):
        players = self.get_players()
        test = []
        # Lists each clue type and takes inputs for selections
        for type, selection in dictionary.items():
            print(f"Select the number corresponding to the {type} provided.")
            selection_array = selection.keys()

            # Takes the nested dictionary within selection, lists options, and takes the input from user
            for i, key in enumerate(selection_array):
                print(f"{i}     {key}")
            order = self.functions.get_int_array(-1, len(selection.keys()), 1)
            selection_list = list(selection_array)

            # Converts int to selection and adds it to an array of the selections made.
            for item in order:
                test.append(selection_list[item])
            print("Selection Array:", selection_list)
            print("Test: ", test)
        
        # Converts all values mentioned to false to players who said no
        if len(players) > 2:
            for player in players[1:-1]:
                self.functions.change_nested_data(player.possibilities, test, False)
                self.functions.display_dictionary(player, player.possibilities)

        # Appends set to player with one of set and marks items as possible
        players[-1].set_list.append(test)
        for player in players:
            player.filter_false()
            print(player.name)
            print(player.set_list)
program = Main()
