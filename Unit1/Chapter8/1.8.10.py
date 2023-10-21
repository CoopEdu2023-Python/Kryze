def sum_of_items(target):
    sum = 0
    for key in target.keys():
        sum += 1
    return sum


dictionary = {1: 1, 2: 2, 3: 3}
print(sum_of_items(dictionary))