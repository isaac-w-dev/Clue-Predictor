from player import Player

class Me(Player):
    def __init__(self):
        self.possibilities = {
    'weapon': {
        'knife': None,
        'gun': None,
        'poison': None,
        'rope': None,
        'hammer': None,
        'sword': None
    },
    'person': {
        'ms_scarlet': None,
        'colonel_mustard': None,
        'mr_green': None,
        'prof_plum': None,
        'mz_peacock': None,
        'mrs_white': None
    },
    'room': {
        'ballroom': None,
        'bathroom': None,
        'billiards_room': None,
        'conservatory': None,
        'greenroom': None,
        'bedroom': None,
        'garden': None,
        'disco_room': None,
        'game_room': None
    }
}
        self.initialize_cards()
        # self.chart_cards()
        
    def initialize_cards(self):
        for clue_type in self.possibilities:
            print(type(clue_type))
            # for item in self.possibilities[clue_type]:
            #     print(type(item))
                # self.possibilities[clue_type].update({item:False})
                # item = False

        print(self.possibilities)

    def enter_your_cards(self):
        your_weapons = []
        your_persons = []
        your_rooms = []

        selection = None
        while selection != 0:
            selection = input('''Which weapons do you have?\nEnter the corresponding number for each weapon you possess:\nKnife- 1\nGun- 2\nPoison- 3\nRope- 4
Hammer- 5\nSword- 6''')
            selection_array = selection.split()
            try:
                for item in selection_array:
                    item = int(item)
            except:
                print('Error converting string to integer. \nRestarting selection process.')

    def chart_attribute(self, clue_type):
        print(clue_type)
        print(f'''Which {clue_type} do you have?\nEnter the corresponding number for each {clue_type} you have.''')
        type = list(self.possibilities[clue_type])
        for i, item in enumerate(type):
            print(i, item)
        user_entry = input().split()
        converted_entry = []
        
        for num in user_entry:
            converted_entry.append(type[int(num)])
        print(converted_entry)

        for item in self.possibilities.values():
            if item in converted_entry:
                item = True

            if item == None:
                item  = False

    def chart_cards(self):
        for item in self.possibilities.keys():
            self.chart_attribute(item)


    #     print(self.possibilities)
        # chart_cards(possibilities['weapon'], 'Weapons')
        # chart_cards(possibilities['person'], 'Persons')
        # chart_cards(possibilities['room'], 'Rooms')