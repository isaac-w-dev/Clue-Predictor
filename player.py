from evidence import evidence
from functions import Functions

import copy
class Player():

    def __init__(self):
        self.set_list = []
        self.possibilities = copy.deepcopy(evidence)
        self.functions = Functions()


    def get_num_cards(self, num_players):
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
            except:
                continue


    def confirm_information(self):
        print(f'''Name: {self.name}\nNumber of cards: {self.num_of_cards}\nIs this correct? Y/N: ''')
        if input().upper() == 'N': return False
        else:
            return True


    def set_variable_attributes(self, num_players):
        while True:
            self.name = input('Enter name of player here: ')
            self.get_num_cards(num_players)

            if self.confirm_information() == True:
                print('Player confirmed!')    
                break
            print('Confirmation failed. Enter the corrected data.')


    def check_commonalities(self):
        freq_dict = {}
        for set in self.set_list:
            for item in set:
                if item in freq_dict: freq_dict.update({item: freq_dict[item] + 1})
                freq_dict.update({item:1})


    def append_set(self, set):
        self.set_list.append(set)