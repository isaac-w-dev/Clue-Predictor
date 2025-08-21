from player import Player

class Me(Player):
    def __init__(self):
        self.name = 'Me'
        self.possibilities = {
    'weapon': {
        'knife': False,
        'gun': False,
        'poison': False,
        'rope': False,
        'hammer': False,
        'sword': False
    },
    'person': {
        'ms_scarlet': False,
        'colonel_mustard': False,
        'mr_green': False,
        'prof_plum': False,
        'mz_peacock': False,
        'mrs_white': False
    },
    'room': {
        'ballroom': False,
        'bathroom': False,
        'billiards_room': False,
        'conservatory': False,
        'greenroom': False,
        'bedroom': False,
        'garden': False,
        'disco_room': False,
        'game_room': False
    }
}
        # self.chart_cards()        

        print(self.possibilities)

    def chart_cards(self):
        your_weapons = []
        your_persons = []
        your_rooms = []

        selection = None
        for key, value in self.possibilities.items():
            self.chart_attribute(key, value)

        
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