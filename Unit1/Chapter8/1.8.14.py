def combine_data(input_keys, input_values):
    output_data = dict()
    num = min(len(input_keys), len(input_values))
    for i in range(num):
        output_data[input_keys[i]] = input_values[i]
    return output_data


raw_keys = ['a', 'b', 'c', 'd', 'e', 'f']
raw_values = [1, 2, 3, 4, 5]
print(combine_data(raw_keys, raw_values))