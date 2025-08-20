class Player():
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
    def set_variable_attributes(self):
        while True:
            self.name = input('Enter name of player here: ')
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
            else:
                print(f'''Name: {self.name}\nNumber of cards: {self.num_of_cards}\nIs this correct? Y/N: ''')
                if input().upper() == 'N':
                    continue
                else: break

    def change_nested_data(self, dictionary, variable, new_value, indent=''):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                print(key)
                self.change_nested_data(value, variable, new_value, indent + '   ')
            else:
                if key == variable:
                    value = new_value
                    dictionary.update({key: value})
            print(f'{indent}{key}: {value}')

