def third_largest_number(target):
    mid_list = list(target)
    mid_list.sort()
    return mid_list[2]


my_set = {1, 2, 9, 4, 5}
print(third_largest_number(my_set))