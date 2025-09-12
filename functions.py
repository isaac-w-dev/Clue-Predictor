class Functions():

    def check_bounds(self, lower, upper, item):
        # Checks if int is within alotted bounds
        if item < lower or item > upper: return False
        return True

    def check_length(self, max_length, array):
        # Checks if the length of the array is within bounds
        if len(array) > max_length: return True
        else: return False

    def check_int(self, checked_item):
        # Checks if entry is an int
        if isinstance(checked_item, int):
            return True
        else: return False

    def validate_int(self, upper, int, lower = 0):
        # Performs all integer checks on entry
        if self.check_int(int) == False:
            print("Not an int")
            return False
        if self.check_bounds(lower, upper, int) == False:
            print("Bounding Error")
            return False
        return True
        
    def get_int_array(self, lower, upper, max_length):
        # Receives int array and does validation checks
        while True:
            int_str = input().split()
            int_array = []
            for value in int_str:
                if self.validate_int(upper, int(value), lower) == True:
                    int_array.append(int(value))
                else:
                    print("Error in selection, enter your selections again.")
            if len(int_array) == max_length:
                return int_array

    def change_nested_data(self, dictionary, array, new_value, indent=''):
        # Changes a value within a dictionary given the key and new value to be changed to
        for key, value in dictionary.items():
            if isinstance(value, dict):
                print(f'{indent}{key}')
                self.change_nested_data(value, array, new_value, indent + '   ')
            else:
                if key in array:
                    value = new_value
                    dictionary.update({key: value})
                print(f'{indent}{key}: {value}')
        print()


    def check_nested_data(self, dictionary, variable, value_checked):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                # print(key)
                self.check_nested_data(value, variable, value_checked)
            else:
                if key == variable:
                    if value == value_checked:
                        return True
        return False

    def display_dictionary(self, player, dictionary, indent =''):
        print(player.name)
        indent += ' '
        for key, value in dictionary.items():
            if isinstance(value, dict):
                print(f'{indent}{key}')
                self.display_dictionary(player, value, indent + '  ')
            else: print(f'{indent}{key}: {value}')

    def chart_attribute(self, clue_type, obj):
        # Returns an array of the clues selected from input integers
        print(f'''Enter the corresponding number for each {clue_type} you have.''')
        type = list(obj)

        for i, item in enumerate(type):
            print(i, item)

        # user_entry = input().split()
        user_entry = ["0", "1"]
        converted_entry = []
        
        for num in user_entry:
            converted_entry.append(type[int(num)])

        return converted_entry


    def chart_cards(self, nested_obj, new_value = True):
        # Charts all possible cards
        evidence = []
        
        for key, value in nested_obj.items():
            evidence += self.chart_attribute(key, value)
        
        self.change_nested_data(nested_obj, evidence, new_value)


    def convert_all_values(self, dictionary, new_value = None):
        # Converts all values in a dictionary to a given value
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.convert_all_values(value, new_value)
            else:
                value = new_value
                dictionary.update({key: value})

    def return_true_values(self, player_dict):
        true_values = []
        for clue_type, sub_dict in player_dict.items():
                for item, value in sub_dict.items():
                    if value == True:
                        true_values.append(item)
        print(true_values)
        return true_values

    def deductions_from_true(self, host_dict, player_array):
        true_values = self.return_true_values(host_dict)
        for player in player_array:
            player.functions.change_nested_data(player.possibilities, true_values, False)