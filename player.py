from evidence import evidence
from functions import Functions

import copy
class Player():

    def __init__(self):
        self.set_list = []
        self.possibilities = copy.deepcopy(evidence)
        self.functions = Functions()


    def get_num_cards(self, num_players):
        # Either calculates the number of cards per player based on the num of players or gets the input per player if 18 is not perfectly divisible by num of players
        if 18 % num_players == 0:
            self.num_of_cards = int(18 / num_players)
            return
        while True:
            try:
                self.num_of_cards = int(input('Enter number of cards player has: '))
                if self.num_of_cards > 6: 
                    print("That's too many cards!")
                    continue
                elif self.num_of_cards < 3:
                    print("That's not enough cards for a game!")
                    continue
                break
            except:
                continue


    def confirm_information(self):
        print(f'''Name: {self.name}\nNumber of cards: {self.num_of_cards}\nIs this correct? Y/N: ''')
        if input().upper() == 'N': return False
        else:
            return True


    # def set_variable_attributes(self, num_players):
    #     # Sets all attributes that may vary for each player from game to game
    #     while True:
    #         self.name = input('Enter name of player here: ')
    #         self.get_num_cards(num_players)

    #         if self.confirm_information() == True:
    #             print('Player confirmed!')    
    #             break
    #         print('Confirmation failed. Enter the corrected data.')



    def set_variable_attributes(self, player_name, num_cards):
        self.name = player_name
        self.num_of_cards = num_cards



    def check_commonalities(self):
        # Creates a dictionary referencing how common an item is in sets the player has responded to
        self.freq_dict = {}
        for set in self.set_list:
            for item in set:
                if item in self.freq_dict: self.freq_dict.update({item: self.freq_dict[item] + 1})
                self.freq_dict.update({item:1})

    def filter_false(self):
        # Filters out any items in each set within the set list if the possibility value is False in the player's dictionary
        for set in self.set_list[:]:
            print("Set before filtering:", set)


            for item in set[:]:
                if self.functions.check_nested_data(self.possibilities, item, False) == True: set.remove(item)

                
            print("Set after filtering: ", set)
            print("Possibilities pre-changes: ", self.possibilities)
            if len(set) == 1:
                self.functions.change_nested_data(self.possibilities, set, True)
            print("Possibilities post-changes: ", self.possibilities)

        # self.functions.display_dictionary(self, self.possibilities)