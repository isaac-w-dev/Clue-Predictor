class Functions():
    def check_bounds(self, lower, upper, array):
        for item in array:
            if item < lower or item > upper: return False
        return True
        
    def get_int(self, lower, upper, max_length):
        while True:
            int_str = input().split()
            int_array = []
            repeat = False
            if len(int_str) > max_length: continue
            for value in int_str:
                try:
                    int_array.append(int(value))
                    if self.check_bounds(lower, upper, int_array) == False: raise Exception("Bounding Error")
                except:
                    repeat = True
            if repeat == False:
                if len(int_array) == 1:
                    return int_array[0]
                return int_array
            else:
                print("Error in selection, try again")

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