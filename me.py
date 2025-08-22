from player import Player
from evidence import evidence
import copy

class Me(Player):
    def __init__(self):
        self.name = 'Me'
        self.set_list = []
        self.possibilities = copy.deepcopy(evidence)
        self.convert_all_values(self.possibilities)
        print("My clues", self.possibilities)
        # self.chart_cards()
        
    def chart_cards(self):
        your_weapons = []
        your_persons = []
        your_rooms = []

        selection = None
        for key, value in self.possibilities.items():
            self.chart_attribute(key, value)

    def convert_all_values(self, dictionary, new_value = False):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                print(key)
                self.convert_all_values(value)
            else:
                dictionary.update({key:new_value})


    def chart_attribute(self, clue_type, obj):
        print(obj)
        print(f'''Enter the corresponding number for each {clue_type} you have.''')
        type = list(obj)
        for i, item in enumerate(type):
            print(i, item)
        user_entry = input().split()
        converted_entry = []
        
        for num in user_entry:
            converted_entry.append(type[int(num)])
        print(converted_entry)

        # for key, value in self.possibilities.items():
        #     for key, item in self.possibilities[value].items():
        #     if item in converted_entry:
        #         item = True


        # print(self.possibilities)
        # chart_cards(possibilities['weapon'], 'Weapons')
        # chart_cards(possibilities['person'], 'Persons')
        # chart_cards(possibilities['room'], 'Rooms')