def sum_list(raw_data):
    sum_of_elements = 0
    for value in raw_data:
        if type(value) in (float, int):
            sum_of_elements += value
        else:
            sum_of_elements += sum_list(value)
    return sum_of_elements


data = [1, 2, [3, 4], [5, 6]]
print(sum_list(data))
