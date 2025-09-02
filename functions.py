class Functions():

    def check_bounds(self, lower, upper, item):
        if item < lower or item > upper: return False
        return True

    def check_length(self, max_length, array):
        if len(array) > max_length: return True
        else: return False

    def check_int(self, checked_item):
        if isinstance(checked_item, int):
            return True
        else: return False

    def validate_int(self, upper, int, lower = 0):
        if self.check_int(int) == False:
            print("Not an int")
            return False
        if self.check_bounds(upper, int, lower) == False:
            print("Bounding Error")
            return False
        return True
        
    def get_int_array(self, upper, lower, max_length):
        while True:
            int_str = input().split()
            int_array = []
            for value in int_str:
                if self.validate_int(upper, value, lower) == True:
                    int_array.append(int(value))
                else:
                    print("Error in selection, enter your selections again.")

    def change_nested_data(self, dictionary, array, new_value, indent=''):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                print(key)
                self.change_nested_data(value, array, new_value, indent + '   ')
            else:
                if key in array:
                    value = new_value
                    dictionary.update({key: value})
            print(f'{indent}{key}: {value}')


    def check_nested_data(self, dictionary, variable):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                print(key)
                self.check_nested_data(value, variable)
            else:
                if key == variable:
                    if value[:8] == 'Possible' or value == None:
                        return True
        return False


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

        return converted_entry


    def chart_cards(self, nested_obj, new_value = True):
        evidence = []
        
        for key, value in nested_obj.items():
            evidence += self.chart_attribute(key, value)
        
        self.change_nested_data(nested_obj, evidence, new_value)


    def convert_all_values(self, dictionary, new_value = None):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.convert_all_values(value)
            else:
                dictionary.update({key:new_value})

