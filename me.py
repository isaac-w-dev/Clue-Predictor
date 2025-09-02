from player import Player
from evidence import evidence
from functions import Functions
import copy

class Me(Player):
    def __init__(self):
        self.name = 'Me'
        self.set_list = []
        self.possibilities = copy.deepcopy(evidence)
        self.functions = Functions()
        self.functions.convert_all_values(self.possibilities, False)

        self.functions.chart_cards(self.possibilities)
        print(self.possibilities)