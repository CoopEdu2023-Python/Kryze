def symmetric_difference(list_of_set):
    mid = set()
    for i in list_of_set:
        mid = mid.symmetric_difference(i)
    return mid


list_of_set = [{1, 2, 3}, {3, 4}, {5, 6}]
print(symmetric_difference(list_of_set))