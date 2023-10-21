def max_min_finder(target, mode):
    if mode == "max":
        maximum = -2147483647
        for i in target:
            maximum = max(maximum, i)
        return maximum
    if mode == "min":
        minimum = 2147483647
        for i in target:
            minimum = min(minimum, i)
        return minimum


my_set = {1, 2, 3, 4, 5}
print(max_min_finder(my_set, "max"))
print(max_min_finder(my_set, "min"))