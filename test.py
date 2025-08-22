def check_commonalities(set_list):
    freq_dict = {}
    for set in set_list:
        for item in set:
            if item in freq_dict:
                freq_dict.update({item: freq_dict[item] + 1})
            else:
                freq_dict.update({item:1})
    return freq_dict

def append_set(set_list, set):
    set_list.append(set)

def remove_from_set(set_list, value):
    for set in set_list:
        for item in set[:]:
            if value == item:
                set.remove(item)

def frequency_to_str(freq_dict):
    for entry in freq_dict.items():
        clue, freq = entry
        potential = f'Possible {freq}x'
        print(clue, potential)
        
array = [['ms_scarlet', 'green_room', 'knife'],['ms_scarlet', 'conservatory', 'knife'], ['ms_scarlet', 'green_room', 'poison']]

append_set(array, ['mz_peacock', 'bathroom', 'wrench'])
frequency_to_str(check_commonalities(array))
remove_from_set(array, 'knife')