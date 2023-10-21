def max_key(input_data):
    keys = []
    maximum = -2147483647
    for key, value in input_data.items():
        if value > maximum:
            keys.clear()
            maximum = value
            keys.append(key)
        elif value == maximum:
            keys.append(key)
    return keys


raw_data = {'Theodore': 22, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
print(max_key(raw_data))