def split_data(input_dict):
    keys = list(input_dict.keys())
    values = list(input_dict.values())
    num_of_items = len(values[0])
    output_list = list()
    for i in range(num_of_items):
        _data = dict()
        for key in keys:
            _data[key] = values[keys.index(key)][i]
        output_list.append(_data)
    return output_list


raw_data = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print(split_data(raw_data))